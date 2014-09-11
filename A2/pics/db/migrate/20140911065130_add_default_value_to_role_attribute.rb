class AddDefaultValueToRoleAttribute < ActiveRecord::Migration
  def up
    change_column_default :users, :role, "player"
  end

  def down
    change_column_default :users, :role, nil
  end
end
