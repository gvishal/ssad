class TagsController < ApplicationController

  def index
    @tags = Tag.all 
  end

  def new
    @tag = Tag.new
  end

  def create
    @tag = Tag.create(params[:tag])
    if @tag.save
      redirect_to tags_path
    else
      render "new"
    end
  end

  def show
    @tag = Tag.find(params[:id])
  end

  def edit
    @tag = Tag.find(params[:id])
  end
  
  def destroy
    Tag.find(params[:id]).destroy
    redirect_to tags_path
  end
end
