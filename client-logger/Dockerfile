FROM alpine:latest
RUN apk add --no-cache curl bash
WORKDIR /app
COPY logger.sh .
RUN chmod +x logger.sh
CMD ["./logger.sh"]
