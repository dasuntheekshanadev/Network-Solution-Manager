# Use a base image with SSH server installed, such as Ubuntu or Debian
FROM ubuntu:latest

# Install SSH server
RUN apt-get update && \
    apt-get install -y openssh-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Create SSH directory
RUN mkdir /var/run/sshd

# Set root password (replace 'password' with your desired password)
RUN echo 'root:password123' | chpasswd

# Expose SSH port
EXPOSE 22

# Start SSH service
CMD ["/usr/sbin/sshd", "-D"]