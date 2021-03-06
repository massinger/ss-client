FROM debian

ENV HAPROXY_VERSION 1.9.6
ENV HAPROXY_URL https://www.haproxy.org/download/1.9/src/haproxy-1.9.6.tar.gz
ENV HAPROXY_SHA256 0837c35e2914d40f685740487886e86b1b16132b81ecb60a3be66cf9a6f19bef


RUN  echo 'deb http://mirrors.tuna.tsinghua.edu.cn/debian/ stretch main contrib non-free \n\
deb http://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-updates main contrib non-free \n\
deb http://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-backports main contrib non-free \n\
deb http://mirrors.tuna.tsinghua.edu.cn/debian-security stretch/updates main contrib non-free\n'>/etc/apt/sources.list
#RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list
# see https://sources.debian.net/src/haproxy/jessie/debian/rules/ for some helpful navigation of the possible "make" arguments
RUN set -x \
	\
	&& savedAptMark="$(apt-mark showmanual)" \
	&& apt-get update && apt-get install -y --no-install-recommends \
		ca-certificates \
		gcc \
		libc6-dev \
		liblua5.3-dev \
		libpcre3-dev \
		libssl-dev \
		make \
		wget \
		zlib1g-dev \
		curl \
	&& rm -rf /var/lib/apt/lists/* \
	\
	&& wget -O haproxy.tar.gz "$HAPROXY_URL" \
	&& echo "$HAPROXY_SHA256 *haproxy.tar.gz" | sha256sum -c \
	&& mkdir -p /usr/src/haproxy \
	&& tar -xzf haproxy.tar.gz -C /usr/src/haproxy --strip-components=1 \
	&& rm haproxy.tar.gz \
	\
	&& makeOpts=' \
		TARGET=linux2628 \
		USE_LUA=1 LUA_INC=/usr/include/lua5.3 \
		USE_OPENSSL=1 \
		USE_PCRE=1 PCREDIR= \
		USE_ZLIB=1 \
	' \
	&& make -C /usr/src/haproxy -j "$(nproc)" all $makeOpts \
	&& make -C /usr/src/haproxy install-bin $makeOpts \
	\
	&& mkdir -p /usr/local/etc/haproxy \
	&& cp -R /usr/src/haproxy/examples/errorfiles /usr/local/etc/haproxy/errors \
	&& rm -rf /usr/src/haproxy
#	\
#	&& apt-mark auto '.*' > /dev/null \
#	&& { [ -z "$savedAptMark" ] || apt-mark manual $savedAptMark; } \
#	&& find /usr/local -type f -executable -exec ldd '{}' ';' \
#		| awk '/=>/ { print $(NF-1) }' \
#		| sort -u \
#		| xargs -r dpkg-query --search \
#		| cut -d: -f1 \
#		| sort -u \
#		| xargs -r apt-mark manual \
#	&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false

# https://www.haproxy.org/download/1.8/doc/management.txt
# "4. Stopping and restarting HAProxy"
# "when the SIGTERM signal is sent to the haproxy process, it immediately quits and all established connections are closed"
# "graceful stop is triggered when the SIGUSR1 signal is sent to the haproxy process"
STOPSIGNAL SIGUSR1
COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]




