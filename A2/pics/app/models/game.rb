class Game < ActiveRecord::Base
  attr_accessible :attempts, :level, :score, :user_id

  belongs_to :user
end
