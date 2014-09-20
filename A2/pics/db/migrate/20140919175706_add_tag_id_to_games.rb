class AddTagIdToGames < ActiveRecord::Migration
  def change
    add_column :games, :tag_id, :integer
  end
end
