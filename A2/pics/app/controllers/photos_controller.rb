class PhotosController < ApplicationController

  def index
    @photos = Photo.all 
  end

  def new
    @photo = Photo.new
  end

  def create
    @photo = Photo.create(params[:photo])
    if @photo.save
      render :action => 'show', :id => @photo.id
    else
      render "new"
    end
  end

  def edit
    @photo = Photo.find(params[:id])
  end

  def update
    params[:photo][:tag_ids] ||= []
    @photo = Photo.find(params[:id])
    if @photo.update_attributes(params[:photo])
      flash.now.alert = "Successfully updated!"
      render :action => 'edit', :id => @photo.id
    else
      flash.now.alert = "Try again!"
      render :action => 'edit', :notice => "Try again!"
    end
  end

  def show
    @photo = Photo.find(params[:id])
  end

  def destroy
    Photo.find(params[:id]).destroy
    redirect_to photos_path, :notice => "Deleted"
  end
end

