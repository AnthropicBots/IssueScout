# =============================================================================
# Build Stage
# =============================================================================

FROM node:22-alpine AS builder

WORKDIR /app

# Copy dependency manifests first for better layer caching.
COPY package*.json ./

# Install dependencies.
RUN npm ci

# Copy application source.
COPY . .

# Build the production bundle.
RUN npm run build

# =============================================================================
# Production Stage
# =============================================================================

FROM nginx:1.29-alpine

# Copy the compiled application.
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose the HTTP port.
EXPOSE 80

# Start Nginx.
CMD ["nginx", "-g", "daemon off;"]
