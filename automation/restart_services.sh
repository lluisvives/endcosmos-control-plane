#!/bin/bash

echo "EndCosmos Control Plane"
echo "Restarting infrastructure services..."

sudo systemctl restart nginx
sudo systemctl restart endcosmos-api
sudo systemctl restart ai-gateway

echo "Services restarted successfully."
