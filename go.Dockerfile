FROM golang:1.21

# Add Tini
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

# Run your program under Tini
# CMD ["/your/program", "-and", "-its", "arguments"]
# or docker run your-image /your/program ...