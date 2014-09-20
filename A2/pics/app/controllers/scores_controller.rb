class ScoresController < ApplicationController
  def index
    @scores = Score.order('score DESC').limit(10)
  end

  def show
    @scores = Score.where("user_id = ?", session[:user_id])
  end
end
