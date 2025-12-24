# STAGE 1: Build process
# Using golang-alpine for a lightweight build environment
FROM golang:1.21-alpine AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy dependency files first to leverage Docker cache
COPY go.mod go.sum ./
RUN go mod download

# Copy the rest of the source code
COPY . .

# Build the application as a static binary
# CGO_ENABLED=0 ensures the binary is statically linked (portable)
# GOOS=linux targets the Linux operating system
RUN CGO_ENABLED=0 GOOS=linux go build -o main .

# STAGE 2: Final runtime image
# Using Alpine Linux for the smallest possible security footprint
FROM alpine:latest

# Install CA certificates for secure communication
RUN apk --no-cache add ca-certificates

# Set the working directory inside the container
WORKDIR /root/

# Copy the compiled binary from the builder stage
# Only copy the compiled binary, leaving the source code behind!
COPY --from=builder /app/main .

# Document the port the application listens on
EXPOSE 8080

# Execute the binary
CMD ["./main"]