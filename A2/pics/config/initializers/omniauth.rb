OmniAuth.config.logger = Rails.logger

Rails.application.config.middleware.use OmniAuth::Builder do
  provider :facebook, '554069478055146', 'c9bafeee6aa62eb556fcd8ec6d867971'
end