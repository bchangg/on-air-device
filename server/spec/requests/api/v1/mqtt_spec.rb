require 'rails_helper'

RSpec.describe 'Api::V1::MqttController', type: :request do
  describe 'POST #publish' do
    it 'publishes light on to the MQTT broker' do
      client = double(MQTT::Client)
      allow(MQTT::Client).to receive(:connect).and_yield(client)

      expect(client).to receive(:publish).with(
        ENV['MQTT_TOPIC'],
        ENV['MQTT_MESSAGE']
      )

      post api_v1_publish_path

      expect(response).to have_http_status(:ok)
    end
  end
end
