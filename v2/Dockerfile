FROM docker.elastic.co/elasticsearch/elasticsearch:7.8.0

# Set environment variables
ENV http.cors.enabled=true \
    http.cors.allow-origin=http://localhost:8080 \
    discovery.type=single-node

# Expose Elasticsearch ports
EXPOSE 9200 9300

# Start Elasticsearch
# CMD ["elasticsearch"]

# Install Elasticvue
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g elasticvue && \
    apt-get remove -y curl && \
    apt-get clean

# Expose Elasticvue port
EXPOSE 8080

# Start Elasticvue
CMD ["elasticsearch","elasticvue"]