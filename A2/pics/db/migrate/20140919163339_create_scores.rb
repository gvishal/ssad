class CreateScores < ActiveRecord::Migration
  def change
    create_table :scores do |t|
      t.references :user
      t.integer :score

      t.timestamps
    end
    add_index :scores, :user_id
  end
end
