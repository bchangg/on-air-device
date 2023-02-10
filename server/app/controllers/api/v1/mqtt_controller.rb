class Api::V1::MqttController < ApplicationController
  def publish
    render plain: 'publish some info to mqtt'
  end
end