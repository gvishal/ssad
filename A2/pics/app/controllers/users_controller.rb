class UsersController < ApplicationController
  before_filter :find_user, :only => [:show, :edit, :update]

  def find_user
    @user = User.find(params[:id])
    rescue ActiveRecord::RecordNotFound
      render_404
  end

  def render_404
    respond_to do |format|
      format.html { render :file => "#{Rails.root}/public/404", :layout => false, :status => :not_found }
      format.xml  { head :not_found }
      format.any  { head :not_found }
    end
  end

  def index
    @users = User.all
  end
  
  def new
    @user = User.new
  end

  def create
    @user = User.new(params[:user])
    if @user.save
      redirect_to root_url, :notice => "Signed up!"
    else
      render "new"
    end
  end

  def show
    @user = User.find(params[:id])
  end

  def edit
    @user = User.find(params[:id])
  end

  def update
    @user = User.find(params[:id])
    if @user.update_attributes(params[:user])
      flash.now.alert = "Successfully updated!"
      render :action => 'edit', :id => @user.id
    else
      flash.now.alert = "Try again!"
      render :action => 'edit', :notice => "Try again!"
    end
  end

  def destroy
    User.find(params[:id]).destroy
    session[:user_id] = nil
    redirect_to root_url, :notice => "Deleted!"
  end
end
