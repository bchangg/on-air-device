class Api::V1::MqttController < ApplicationController
  def publish
    MQTT::Client.connect(
      host: ENV['MQTT_HOST'],
      username: ENV['MQTT_USERNAME'],
      password: ENV['MQTT_PASSWORD'],
      ssl: true
    ) do |client|
      client.publish(ENV['MQTT_TOPIC'], ENV['MQTT_MESSAGE'])
    end

    render json: {
      success: true,
      topic: ENV['MQTT_TOPIC'],
      message: ENV['MQTT_MESSAGE']
    }, status: :ok
  rescue => e
    render json: {
      success: false,
      message: e
    }, status: :not_acceptable
  end
end
