class Photo < ActiveRecord::Base
  attr_accessible :image,:tag_ids

  has_and_belongs_to_many :tags

  has_attached_file :image, styles: { small: "100x100", med: "200x200", large: "400x400" },
                  :url  => "/assets/:id/:style/:basename.:extension",
                  :path => ":rails_root/public/assets/:id/:style/:basename.:extension"

  validates_attachment_presence :image
  validates_attachment_size :image, :less_than => 5.megabytes
  validates_attachment_content_type :image, :content_type => ['image/jpeg', 'image/png']
end
