---
id: learning.zephyr-docs.api-source-device-reference.page-26
title: net_compat.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__compat_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_net\_compat.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net__compat_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_supplement_reference/P077_zephyr__net__net_compat.h_文件参考.md)。

## 26.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00322"></a>
<a id="l00326"></a>
<a id="l00327"></a>

```c


/*
 * Copyright (c) 2025 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_NET_COMPAT_H_
#define ZEPHYR_INCLUDE_NET_NET_COMPAT_H_


/* No need to generate documentation for the compatibility mode symbols */

#ifdef __cplusplus
extern "C" {
#endif

/* Prevent direct inclusion of this file. This is a private header
 * meant to be included via <net/net_ip.h>.
 */
#if !defined(ZEPHYR_INCLUDE_NET_COMPAT_MODE_SYMBOLS)
#error "This header file should not be included directly. " \
        "Include <zephyr/net/net_ip.h> instead."
#endif /* !defined(ZEPHYR_INCLUDE_NET_COMPAT_MODE_SYMBOLS) */

#define PF_UNSPEC   NET_PF_UNSPEC
#define PF_INET     NET_PF_INET
#define PF_INET6    NET_PF_INET6
#define PF_PACKET   NET_PF_PACKET
#define PF_CAN      NET_PF_CAN
#define PF_NET_MGMT NET_PF_NET_MGMT
#define PF_LOCAL    NET_PF_LOCAL
#define PF_UNIX     NET_PF_UNIX

#define AF_UNSPEC      NET_PF_UNSPEC
#define AF_INET        NET_PF_INET
#define AF_INET6       NET_PF_INET6
#define AF_PACKET      NET_PF_PACKET
#define AF_CAN         NET_PF_CAN
#define AF_NET_MGMT    NET_PF_NET_MGMT
#define AF_LOCAL       NET_PF_LOCAL
#define AF_UNIX        NET_PF_UNIX

#define IPPROTO_IP        NET_IPPROTO_IP
#define IPPROTO_ICMP      NET_IPPROTO_ICMP
#define IPPROTO_IGMP      NET_IPPROTO_IGMP
#define IPPROTO_ETH_P_ALL NET_IPPROTO_ETH_P_ALL
#define IPPROTO_IPIP      NET_IPPROTO_IPIP
#define IPPROTO_TCP       NET_IPPROTO_TCP
#define IPPROTO_UDP       NET_IPPROTO_UDP
#define IPPROTO_IPV6      NET_IPPROTO_IPV6
#define IPPROTO_ICMPV6    NET_IPPROTO_ICMPV6
#define IPPROTO_RAW       NET_IPPROTO_RAW
#define IPPROTO_TLS_1_0   NET_IPPROTO_TLS_1_0
#define IPPROTO_TLS_1_1   NET_IPPROTO_TLS_1_1
#define IPPROTO_TLS_1_2   NET_IPPROTO_TLS_1_2
#define IPPROTO_TLS_1_3   NET_IPPROTO_TLS_1_3
#define IPPROTO_DTLS_1_0  NET_IPPROTO_DTLS_1_0
#define IPPROTO_DTLS_1_2  NET_IPPROTO_DTLS_1_2

#define SOCK_STREAM NET_SOCK_STREAM
#define SOCK_DGRAM  NET_SOCK_DGRAM
#define SOCK_RAW    NET_SOCK_RAW

#define CAN_RAW NET_CAN_RAW
#define SOL_CAN_RAW  (NET_SOL_CAN_BASE + NET_CAN_RAW)
#define CAN_RAW_FILTER NET_CAN_RAW_FILTER

#define ntohs(x)  net_ntohs(x)
#define ntohl(x)  net_ntohl(x)
#define ntohll(x) net_ntohll(x)
#define htons(x)  net_htons(x)
#define htonl(x)  net_htonl(x)
#define htonll(x) net_htonll(x)

#define in_addr  net_in_addr
#define in6_addr net_in6_addr

#define sockaddr         net_sockaddr
#define sockaddr_in      net_sockaddr_in
#define sockaddr_in6     net_sockaddr_in6
#define sockaddr_ll      net_sockaddr_ll
#define sockaddr_can     net_sockaddr_can
#define sockaddr_un      net_sockaddr_un
#define sockaddr_nm      net_sockaddr_nm
#define sockaddr_ptr     net_sockaddr_ptr
#define sockaddr_in_ptr  net_sockaddr_in_ptr
#define sockaddr_in6_ptr net_sockaddr_in6_ptr
#define sockaddr_ll_ptr  net_sockaddr_ll_ptr
#define sockaddr_un_ptr  net_sockaddr_un_ptr
#define sockaddr_can_ptr net_sockaddr_can_ptr
#define sockaddr_storage net_sockaddr_storage

#define sa_family_t   net_sa_family_t
#define socklen_t     net_socklen_t

#define iovec                     net_iovec
#define msghdr                    net_msghdr
#define cmsghdr                   net_cmsghdr
#define ALIGN_H(x)                NET_ALIGN_H(x)
#define ALIGN_D(x)                NET_ALIGN_D(x)
#define CMSG_LEN(len)             NET_CMSG_LEN(len)
#define CMSG_SPACE(len)           NET_CMSG_SPACE(len)
#define CMSG_DATA(cmsg)           NET_CMSG_DATA(cmsg)
#define CMSG_FIRSTHDR(msghdr)     NET_CMSG_FIRSTHDR(msghdr)
#define CMSG_NXTHDR(msghdr, cmsg) NET_CMSG_NXTHDR(msghdr, cmsg)

#define PACKET_HOST       NET_PACKET_HOST
#define PACKET_BROADCAST  NET_PACKET_BROADCAST
#define PACKET_MULTICAST  NET_PACKET_MULTICAST
#define PACKET_OTHERHOST  NET_PACKET_OTHERHOST
#define PACKET_OUTGOING   NET_PACKET_OUTGOING
#define PACKET_LOOPBACK   NET_PACKET_LOOPBACK
#define PACKET_FASTROUTE  NET_PACKET_FASTROUTE

#define in6addr_any       net_in6addr_any
#define in6addr_loopback  net_in6addr_loopback

#define INADDR_ANY             NET_INADDR_ANY
#define INADDR_BROADCAST       NET_INADDR_BROADCAST
#define INADDR_ANY_INIT        NET_INADDR_ANY_INIT
#define INADDR_LOOPBACK_INIT   NET_INADDR_LOOPBACK_INIT
#define INET_ADDRSTRLEN        NET_INET_ADDRSTRLEN
#define INET6_ADDRSTRLEN       NET_INET6_ADDRSTRLEN
#define IN6ADDR_ANY_INIT       NET_IN6ADDR_ANY_INIT
#define IN6ADDR_LOOPBACK_INIT  NET_IN6ADDR_LOOPBACK_INIT

#if !defined(IFNAMSIZ)
#define IFNAMSIZ NET_IFNAMSIZ
#endif /* IFNAMSIZ */

#define in_pktinfo   net_in_pktinfo
#define ip_mreqn     net_ip_mreqn
#define ip_mreq      net_ip_mreq
#define ipv6_mreq    net_ipv6_mreq
#define packet_mreq  net_packet_mreq
#define in6_pktinfo  net_in6_pktinfo
#define ifreq        net_ifreq

#define SOL_TLS                           ZSOCK_SOL_TLS
#define TLS_SEC_TAG_LIST                  ZSOCK_TLS_SEC_TAG_LIST
#define TLS_HOSTNAME                      ZSOCK_TLS_HOSTNAME
#define TLS_CIPHERSUITE_LIST              ZSOCK_TLS_CIPHERSUITE_LIST
#define TLS_CIPHERSUITE_USED              ZSOCK_TLS_CIPHERSUITE_USED
#define TLS_PEER_VERIFY                   ZSOCK_TLS_PEER_VERIFY
#define TLS_DTLS_ROLE                     ZSOCK_TLS_DTLS_ROLE
#define TLS_ALPN_LIST                     ZSOCK_TLS_ALPN_LIST
#define TLS_DTLS_HANDSHAKE_TIMEOUT_MIN    ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MIN
#define TLS_DTLS_HANDSHAKE_TIMEOUT_MAX    ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MAX
#define TLS_CERT_NOCOPY                   ZSOCK_TLS_CERT_NOCOPY
#define TLS_NATIVE                        ZSOCK_TLS_NATIVE
#define TLS_SESSION_CACHE                 ZSOCK_TLS_SESSION_CACHE
#define TLS_SESSION_CACHE_PURGE           ZSOCK_TLS_SESSION_CACHE_PURGE
#define TLS_DTLS_CID                      ZSOCK_TLS_DTLS_CID
#define TLS_DTLS_CID_STATUS               ZSOCK_TLS_DTLS_CID_STATUS
#define TLS_DTLS_CID_VALUE                ZSOCK_TLS_DTLS_CID_VALUE
#define TLS_DTLS_PEER_CID_VALUE           ZSOCK_TLS_DTLS_PEER_CID_VALUE
#define TLS_DTLS_HANDSHAKE_ON_CONNECT     ZSOCK_TLS_DTLS_HANDSHAKE_ON_CONNECT
#define TLS_CERT_VERIFY_RESULT            ZSOCK_TLS_CERT_VERIFY_RESULT
#define TLS_CERT_VERIFY_CALLBACK          ZSOCK_TLS_CERT_VERIFY_CALLBACK
#define TLS_MAX_FRAGMENT_LENGTH           ZSOCK_TLS_MAX_FRAGMENT_LENGTH
#define TLS_PEER_VERIFY_NONE              ZSOCK_TLS_PEER_VERIFY_NONE
#define TLS_PEER_VERIFY_OPTIONAL          ZSOCK_TLS_PEER_VERIFY_OPTIONAL
#define TLS_PEER_VERIFY_REQUIRED          ZSOCK_TLS_PEER_VERIFY_REQUIRED
#define TLS_DTLS_ROLE_CLIENT              ZSOCK_TLS_DTLS_ROLE_CLIENT
#define TLS_DTLS_ROLE_SERVER              ZSOCK_TLS_DTLS_ROLE_SERVER
#define TLS_CERT_NOCOPY_NONE              ZSOCK_TLS_CERT_NOCOPY_NONE
#define TLS_CERT_NOCOPY_OPTIONAL          ZSOCK_TLS_CERT_NOCOPY_OPTIONAL
#define TLS_SESSION_CACHE_DISABLED        ZSOCK_TLS_SESSION_CACHE_DISABLED
#define TLS_SESSION_CACHE_ENABLED         ZSOCK_TLS_SESSION_CACHE_ENABLED
#define TLS_DTLS_CID_DISABLED             ZSOCK_TLS_DTLS_CID_DISABLED
#define TLS_DTLS_CID_SUPPORTED            ZSOCK_TLS_DTLS_CID_SUPPORTED
#define TLS_DTLS_CID_ENABLED              ZSOCK_TLS_DTLS_CID_ENABLED
#define TLS_DTLS_CID_STATUS_DISABLED      ZSOCK_TLS_DTLS_CID_STATUS_DISABLED
#define TLS_DTLS_CID_STATUS_DOWNLINK      ZSOCK_TLS_DTLS_CID_STATUS_DOWNLINK
#define TLS_DTLS_CID_STATUS_UPLINK        ZSOCK_TLS_DTLS_CID_STATUS_UPLINK
#define TLS_DTLS_CID_STATUS_BIDIRECTIONAL ZSOCK_TLS_DTLS_CID_STATUS_BIDIRECTIONAL
#define TLS_MFL_DISABLED                  ZSOCK_TLS_MFL_DISABLED
#define TLS_MFL_512                       ZSOCK_TLS_MFL_512
#define TLS_MFL_1024                      ZSOCK_TLS_MFL_1024
#define TLS_MFL_2048                      ZSOCK_TLS_MFL_2048
#define TLS_MFL_4096                      ZSOCK_TLS_MFL_4096

#define tls_cert_verify_cb zsock_tls_cert_verify_cb

#define AI_PASSIVE      ZSOCK_AI_PASSIVE
#define AI_CANONNAME    ZSOCK_AI_CANONNAME
#define AI_NUMERICHOST  ZSOCK_AI_NUMERICHOST
#define AI_V4MAPPED     ZSOCK_AI_V4MAPPED
#define AI_ALL          ZSOCK_AI_ALL
#define AI_ADDRCONFIG   ZSOCK_AI_ADDRCONFIG
#define AI_NUMERICSERV  ZSOCK_AI_NUMERICSERV
#define AI_EXTFLAGS     ZSOCK_AI_EXTFLAGS

#define NI_NUMERICHOST  ZSOCK_NI_NUMERICHOST
#define NI_NUMERICSERV  ZSOCK_NI_NUMERICSERV
#define NI_NOFQDN       ZSOCK_NI_NOFQDN
#define NI_NAMEREQD     ZSOCK_NI_NAMEREQD
#define NI_DGRAM        ZSOCK_NI_DGRAM
#define NI_MAXHOST      ZSOCK_NI_MAXHOST

#define SOL_SOCKET                    ZSOCK_SOL_SOCKET
#define SO_DEBUG                      ZSOCK_SO_DEBUG
#define SO_REUSEADDR                  ZSOCK_SO_REUSEADDR
#define SO_TYPE                       ZSOCK_SO_TYPE
#define SO_ERROR                      ZSOCK_SO_ERROR
#define SO_DONTROUTE                  ZSOCK_SO_DONTROUTE
#define SO_BROADCAST                  ZSOCK_SO_BROADCAST
#define SO_SNDBUF                     ZSOCK_SO_SNDBUF
#define SO_RCVBUF                     ZSOCK_SO_RCVBUF
#define SO_KEEPALIVE                  ZSOCK_SO_KEEPALIVE
#define SO_OOBINLINE                  ZSOCK_SO_OOBINLINE
#define SO_PRIORITY                   ZSOCK_SO_PRIORITY
#define SO_LINGER                     ZSOCK_SO_LINGER
#define SO_REUSEPORT                  ZSOCK_SO_REUSEPORT
#define SO_RCVLOWAT                   ZSOCK_SO_RCVLOWAT
#define SO_SNDLOWAT                   ZSOCK_SO_SNDLOWAT
#define SO_RCVTIMEO                   ZSOCK_SO_RCVTIMEO
#define SO_SNDTIMEO                   ZSOCK_SO_SNDTIMEO
#define SO_BINDTODEVICE               ZSOCK_SO_BINDTODEVICE
#define SO_ACCEPTCONN                 ZSOCK_SO_ACCEPTCONN
#define SO_TIMESTAMPING               ZSOCK_SO_TIMESTAMPING
#define SO_PROTOCOL                   ZSOCK_SO_PROTOCOL
#define SO_DOMAIN                     ZSOCK_SO_DOMAIN
#define SO_SOCKS5                     ZSOCK_SO_SOCKS5
#define SO_TXTIME                     ZSOCK_SO_TXTIME
#define SCM_TXTIME                    ZSOCK_SCM_TXTIME
#define SOF_TIMESTAMPING_RX_HARDWARE  ZSOCK_SOF_TIMESTAMPING_RX_HARDWARE
#define SOF_TIMESTAMPING_TX_HARDWARE  ZSOCK_SOF_TIMESTAMPING_TX_HARDWARE

#define SHUT_RD   ZSOCK_SHUT_RD
#define SHUT_WR   ZSOCK_SHUT_WR
#define SHUT_RDWR ZSOCK_SHUT_RDWR

#define MSG_PEEK     ZSOCK_MSG_PEEK
#define MSG_TRUNC    ZSOCK_MSG_TRUNC
#define MSG_DONTWAIT ZSOCK_MSG_DONTWAIT
#define MSG_WAITALL  ZSOCK_MSG_WAITALL

#define TCP_NODELAY    ZSOCK_TCP_NODELAY
#define TCP_KEEPIDLE   ZSOCK_TCP_KEEPIDLE
#define TCP_KEEPINTVL  ZSOCK_TCP_KEEPINTVL
#define TCP_KEEPCNT    ZSOCK_TCP_KEEPCNT

#define IP_TOS               ZSOCK_IP_TOS
#define IP_TTL               ZSOCK_IP_TTL
#define IP_PKTINFO           ZSOCK_IP_PKTINFO
#define IP_RECVTTL           ZSOCK_IP_RECVTTL
#define IP_MTU               ZSOCK_IP_MTU
#define IP_MULTICAST_IF      ZSOCK_IP_MULTICAST_IF
#define IP_MULTICAST_TTL     ZSOCK_IP_MULTICAST_TTL
#define IP_MULTICAST_LOOP    ZSOCK_IP_MULTICAST_LOOP
#define IP_ADD_MEMBERSHIP    ZSOCK_IP_ADD_MEMBERSHIP
#define IP_DROP_MEMBERSHIP   ZSOCK_IP_DROP_MEMBERSHIP
#define IP_LOCAL_PORT_RANGE  ZSOCK_IP_LOCAL_PORT_RANGE

#define IPV6_UNICAST_HOPS               ZSOCK_IPV6_UNICAST_HOPS
#define IPV6_MULTICAST_IF               ZSOCK_IPV6_MULTICAST_IF
#define IPV6_MULTICAST_HOPS             ZSOCK_IPV6_MULTICAST_HOPS
#define IPV6_MULTICAST_LOOP             ZSOCK_IPV6_MULTICAST_LOOP
#define IPV6_ADD_MEMBERSHIP             ZSOCK_IPV6_ADD_MEMBERSHIP
#define IPV6_DROP_MEMBERSHIP            ZSOCK_IPV6_DROP_MEMBERSHIP
#define IPV6_JOIN_GROUP                 ZSOCK_IPV6_ADD_MEMBERSHIP
#define IPV6_LEAVE_GROUP                ZSOCK_IPV6_DROP_MEMBERSHIP
#define IPV6_MTU                        ZSOCK_IPV6_MTU
#define IPV6_V6ONLY                     ZSOCK_IPV6_V6ONLY
#define IPV6_RECVPKTINFO                ZSOCK_IPV6_RECVPKTINFO
#define IPV6_PKTINFO                    ZSOCK_IPV6_PKTINFO
#define IPV6_RECVHOPLIMIT               ZSOCK_IPV6_RECVHOPLIMIT
#define IPV6_HOPLIMIT                   ZSOCK_IPV6_HOPLIMIT
#define IPV6_ADDR_PREFERENCES           ZSOCK_IPV6_ADDR_PREFERENCES
#define IPV6_PREFER_SRC_TMP             ZSOCK_IPV6_PREFER_SRC_TMP
#define IPV6_PREFER_SRC_PUBLIC          ZSOCK_IPV6_PREFER_SRC_PUBLIC
#define IPV6_PREFER_SRC_PUBTMP_DEFAULT  ZSOCK_IPV6_PREFER_SRC_PUBTMP_DEFAULT
#define IPV6_PREFER_SRC_COA             ZSOCK_IPV6_PREFER_SRC_COA
#define IPV6_PREFER_SRC_HOME            ZSOCK_IPV6_PREFER_SRC_HOME
#define IPV6_PREFER_SRC_CGA             ZSOCK_IPV6_PREFER_SRC_CGA
#define IPV6_PREFER_SRC_NONCGA          ZSOCK_IPV6_PREFER_SRC_NONCGA
#define IPV6_TCLASS                     ZSOCK_IPV6_TCLASS

#define SOL_PACKET             ZSOCK_SOL_PACKET
#define PACKET_ADD_MEMBERSHIP  ZSOCK_PACKET_ADD_MEMBERSHIP
#define PACKET_DROP_MEMBERSHIP ZSOCK_PACKET_DROP_MEMBERSHIP
#define PACKET_MR_MULTICAST    NET_PACKET_MR_MULTICAST
#define PACKET_MR_PROMISC      NET_PACKET_MR_PROMISC
#define PACKET_MR_ALLMULTI     NET_PACKET_MR_ALLMULTI

#define SOMAXCONN ZSOCK_SOMAXCONN

#define IN6_IS_ADDR_UNSPECIFIED(addr)   ZSOCK_IN6_IS_ADDR_UNSPECIFIED(addr)
#define IN6_IS_ADDR_LOOPBACK(addr)      ZSOCK_IN6_IS_ADDR_LOOPBACK(addr)
#define IN6_IS_ADDR_MULTICAST(addr)     ZSOCK_IN6_IS_ADDR_MULTICAST(addr)
#define IN6_IS_ADDR_LINKLOCAL(addr)     ZSOCK_IN6_IS_ADDR_LINKLOCAL(addr)
#define IN6_IS_ADDR_SITELOCAL(addr)     ZSOCK_IN6_IS_ADDR_SITELOCAL(addr)
#define IN6_IS_ADDR_V4MAPPED(addr)      ZSOCK_IN6_IS_ADDR_V4MAPPED(addr)
#define IN6_IS_ADDR_MC_GLOBAL(addr)     ZSOCK_IN6_IS_ADDR_MC_GLOBAL(addr)
#define IN6_IS_ADDR_MC_NODELOCAL(addr)  ZSOCK_IN6_IS_ADDR_MC_NODELOCAL(addr)
#define IN6_IS_ADDR_MC_LINKLOCAL(addr)  ZSOCK_IN6_IS_ADDR_MC_LINKLOCAL(addr)
#define IN6_IS_ADDR_MC_SITELOCAL(addr)  ZSOCK_IN6_IS_ADDR_MC_SITELOCAL(addr)
#define IN6_IS_ADDR_MC_ORGLOCAL(addr)   ZSOCK_IN6_IS_ADDR_MC_ORGLOCAL(addr)

#ifdef __cplusplus
}
#endif



#endif /* ZEPHYR_INCLUDE_NET_NET_COMPAT_H_ */
```

## 26.2\_可见注释译文（Comments）

### 注释 1：原第 8 行

版权（Copyright）：© 2025 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 26 行

无需为兼容模式符号（Compatibility Mode Symbols）生成文档。

### 注释 3：原第 33 行

禁止直接包含本文件。它是私有头文件（Private Header），应通过 `<net/net_ip.h>` 包含。

### 注释 4：原第 39 行

条件编译（Conditional Compilation）：`!defined(ZEPHYR_INCLUDE_NET_COMPAT_MODE_SYMBOLS)`。

### 注释 5：原第 145 行

接口名称长度标识（Interface Name Size）：`IFNAMSIZ`。

### 注释 6：原第 327 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_NET_COMPAT_H_`。

## 26.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_supplement_reference/P077_zephyr__net__net_compat.h_文件参考.md)

---

[上一章](P025_microchip-sam-gpio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P027_net_pkt_filter.h_源码浏览.md)
