class CreateGames < ActiveRecord::Migration
  def change
    create_table :games do |t|
      t.integer :level
      t.integer :score
      t.integer :attempts

      t.timestamps
    end
  end
end
