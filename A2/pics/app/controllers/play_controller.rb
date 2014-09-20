class PlayController < ApplicationController

  before_filter :current_user, :only => [:index,:create]

  def index
    if not current_user.game
      g = Game.create()
      @current_user.game = g
    end

    tag_id = current_tag
    if not tag_id
      tag_id = Tag.pluck(:id).shuffle[0]
    end

    tag = Tag.find(tag_id)
    while tag.photos.count < 1 do
      tag_id = Tag.pluck(:id).shuffle[0]
      tag = Tag.find(tag_id)
    end

    set_current_tag(tag_id)
    @photos = tag.photos
    @salt = BCrypt::Engine.generate_salt()
    @answer = BCrypt::Engine.hash_secret(tag.name, @salt)
  end

  def create
    answer = params[:answer]
    salt = params[:salt]
    user_answer = params[:user_answer]
    if answer == BCrypt::Engine.hash_secret(user_answer, salt)
      set_current_tag(nil)
      increase_score
      increase_level
      @message = "Correct!"
      redirect_to play_index_url, :notice => "Correct!"
    else
      if current_attempts == 2
        score = Score.create()
        score.score = current_score
        score.user_id = @current_user.id
        score.save!
        s = @current_user.scores
        s.append(score)
        @current_user.scores = s
        @current_user.save!
        increase_attempts
        decrease_score
        reset_game
        redirect_to root_url, :notice => "Game Over"
      else
        increase_attempts
        decrease_score
        redirect_to play_index_url, :notice => "Incorrect Answer"
      end
    end
  end

  private

  def current_user
    if session[:user_id]
      @current_user ||= User.find(session[:user_id])
    else
      redirect_to log_in_path, :notice => "Please login to play!"
    end
  end

  def reset_game
    @current_user.game.attempts = 0
    @current_user.game.score = 0
    @current_user.game.level = 0
    @current_user.game.tag_id = nil
    @current_user.game.save!
  end

  def current_tag
    @current_user.game.tag_id
  end

  def set_current_tag(tag_id)
    @current_user.game.tag_id = tag_id
    @current_user.game.save!
  end


  def increase_attempts
    @current_user.game.increment!(:attempts, by = 1)
  end

  def current_attempts
    @current_user.game.attempts
  end

  def current_score
    @current_user.game.score
  end

  def increase_score
    @current_user.game.increment!(:score, by = 3)
  end

  def decrease_score
    @current_user.game.decrement!(:score, by = 1)
  end

  def current_level
    @current_user.game.level
  end

  def increase_level
    @current_user.game.increment!(:level, by = 1)
  end
end