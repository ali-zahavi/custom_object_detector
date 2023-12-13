echo 'source .env || true' >> ~/.bashrc

# Execute the original entry point
exec "$@"