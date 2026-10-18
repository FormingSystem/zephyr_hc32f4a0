---
id: learning.zephyr-docs.api-file-reference.page-142
title: zephyr__posix__net__if_arp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/if__arp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第142章\_zephyr\_\_posix\_\_net\_\_if\_arp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/if__arp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 142.1\_宏定义（Macros）

<a id="r_ae1acb8a91a94d38dd411fb5e719f35b0"></a>

```c
#define ARPHRD_NETROM 0 /* From KA9Q: NET/ROM pseudo. */
```

相关声明：[ARPHRD_NETROM](#ae1acb8a91a94d38dd411fb5e719f35b0)。

<a id="r_a99b0f33012409144fc0b51bfa835dcba"></a>

```c
#define ARPHRD_ETHER 1 /* Ethernet 10/100Mbps. */
```

相关声明：[ARPHRD_ETHER](#a99b0f33012409144fc0b51bfa835dcba)。

<a id="r_aa2d3040a4ca3fa7aa832b0863bb032a4"></a>

```c
#define ARPHRD_EETHER 2 /* Experimental Ethernet. */
```

相关声明：[ARPHRD_EETHER](#aa2d3040a4ca3fa7aa832b0863bb032a4)。

<a id="r_aeaba33578b2449674b76cd29692a687c"></a>

```c
#define ARPHRD_AX25 3 /* AX.25 Level 2. */
```

相关声明：[ARPHRD_AX25](#aeaba33578b2449674b76cd29692a687c)。

<a id="r_a394dfc37c8b6c429af9d6562a76b0c99"></a>

```c
#define ARPHRD_PRONET 4 /* PROnet token ring. */
```

相关声明：[ARPHRD_PRONET](#a394dfc37c8b6c429af9d6562a76b0c99)。

<a id="r_a6b5310b0311353a79e66f7700ce88e8d"></a>

```c
#define ARPHRD_CHAOS 5 /* Chaosnet. */
```

相关声明：[ARPHRD_CHAOS](#a6b5310b0311353a79e66f7700ce88e8d)。

<a id="r_a63153ce22626e108b5046b89d918803f"></a>

```c
#define ARPHRD_IEEE802 6 /* IEEE 802.2 Ethernet/TR/TB. */
```

相关声明：[ARPHRD_IEEE802](#a63153ce22626e108b5046b89d918803f)。

<a id="r_ade606bd55e7f4f0a03278eed4a8badf8"></a>

```c
#define ARPHRD_ARCNET 7 /* ARCnet. */
```

相关声明：[ARPHRD_ARCNET](#ade606bd55e7f4f0a03278eed4a8badf8)。

<a id="r_a7614228ba176316183dc2ccd61134b6a"></a>

```c
#define ARPHRD_APPLETLK 8 /* APPLEtalk. */
```

相关声明：[ARPHRD_APPLETLK](#a7614228ba176316183dc2ccd61134b6a)。

<a id="r_af02df7fa9173bc0716fe46eb5d45c3e1"></a>

```c
#define ARPHRD_DLCI 15 /* Frame Relay DLCI. */
```

相关声明：[ARPHRD_DLCI](#af02df7fa9173bc0716fe46eb5d45c3e1)。

<a id="r_a52fe51e586dd5952a78a42de1a2992e8"></a>

```c
#define ARPHRD_ATM 19 /* ATM. */
```

相关声明：[ARPHRD_ATM](#a52fe51e586dd5952a78a42de1a2992e8)。

<a id="r_ad597c946041d8b4d02b41c3b2145e10a"></a>

```c
#define ARPHRD_METRICOM 23 /* Metricom STRIP (new IANA id). */
```

相关声明：[ARPHRD_METRICOM](#ad597c946041d8b4d02b41c3b2145e10a)。

<a id="r_a4d072593e2ce7018e74f42eab74b1506"></a>

```c
#define ARPHRD_IEEE1394 24 /* IEEE 1394 IPv4 - RFC 2734. */
```

相关声明：[ARPHRD_IEEE1394](#a4d072593e2ce7018e74f42eab74b1506)。

<a id="r_abbc7280c99b6907038c8e2a433091133"></a>

```c
#define ARPHRD_EUI64 27 /* EUI-64. */
```

相关声明：[ARPHRD_EUI64](#abbc7280c99b6907038c8e2a433091133)。

<a id="r_abb8ca5a62f0f53187a295f0e96ba208b"></a>

```c
#define ARPHRD_INFINIBAND 32 /* InfiniBand. */
```

相关声明：[ARPHRD_INFINIBAND](#abb8ca5a62f0f53187a295f0e96ba208b)。

<a id="r_a45d939a8b7cfeb1145cc5a49f6d2a399"></a>

```c
#define ARPHRD_SLIP 256
```

相关声明：[ARPHRD_SLIP](#a45d939a8b7cfeb1145cc5a49f6d2a399)。

<a id="r_a6651e9c8291dccd470c9426986a160ad"></a>

```c
#define ARPHRD_CSLIP 257
```

相关声明：[ARPHRD_CSLIP](#a6651e9c8291dccd470c9426986a160ad)。

<a id="r_ae35c4cbe46fc19d363a7af42c6dcf273"></a>

```c
#define ARPHRD_SLIP6 258
```

相关声明：[ARPHRD_SLIP6](#ae35c4cbe46fc19d363a7af42c6dcf273)。

<a id="r_ab05b137e1709daec52097cd07d9c86c7"></a>

```c
#define ARPHRD_CSLIP6 259
```

相关声明：[ARPHRD_CSLIP6](#ab05b137e1709daec52097cd07d9c86c7)。

<a id="r_af34e0978e6bb11cf230b5b691a5a1b8a"></a>

```c
#define ARPHRD_RSRVD 260 /* Notional KISS type. */
```

相关声明：[ARPHRD_RSRVD](#af34e0978e6bb11cf230b5b691a5a1b8a)。

<a id="r_a74df13d4969bcad5e7bf0db3706dc388"></a>

```c
#define ARPHRD_ADAPT 264
```

相关声明：[ARPHRD_ADAPT](#a74df13d4969bcad5e7bf0db3706dc388)。

<a id="r_aea2aa154ca4cc488c86727dc44b36b19"></a>

```c
#define ARPHRD_ROSE 270
```

相关声明：[ARPHRD_ROSE](#aea2aa154ca4cc488c86727dc44b36b19)。

<a id="r_a1faa7cf295013abcee809dc908d9be6b"></a>

```c
#define ARPHRD_X25 271 /* CCITT X.25. */
```

相关声明：[ARPHRD_X25](#a1faa7cf295013abcee809dc908d9be6b)。

<a id="r_a0eb9519f0ea218877755913bb4533091"></a>

```c
#define ARPHRD_HWX25 272 /* Boards with X.25 in firmware. */
```

相关声明：[ARPHRD_HWX25](#a0eb9519f0ea218877755913bb4533091)。

<a id="r_a07220dd6d6e255e11f0ea1cf99feba0d"></a>

```c
#define ARPHRD_CAN 280 /* Controller Area Network. */
```

相关声明：[ARPHRD_CAN](#a07220dd6d6e255e11f0ea1cf99feba0d)。

<a id="r_ab490545ded34d438fe2fcc1eaaa39c1e"></a>

```c
#define ARPHRD_MCTP 290
```

相关声明：[ARPHRD_MCTP](#ab490545ded34d438fe2fcc1eaaa39c1e)。

<a id="r_a18dec8be041946b4a3a75ec73bb4293c"></a>

```c
#define ARPHRD_PPP 512
```

相关声明：[ARPHRD_PPP](#a18dec8be041946b4a3a75ec73bb4293c)。

<a id="r_a410eced86d38da357b0ffb10adba4ca2"></a>

```c
#define ARPHRD_CISCO 513 /* Cisco HDLC. */
```

相关声明：[ARPHRD_CISCO](#a410eced86d38da357b0ffb10adba4ca2)。

<a id="r_a8e2c80f4cd4774f76cd7803ba31b27e1"></a>

```c
#define ARPHRD_HDLC ARPHRD_CISCO
```

相关声明：[ARPHRD_HDLC](#a8e2c80f4cd4774f76cd7803ba31b27e1)、[ARPHRD_CISCO](#a410eced86d38da357b0ffb10adba4ca2)。

<a id="r_af09e5ae697b5b32f1e9d053b22a2642c"></a>

```c
#define ARPHRD_LAPB 516 /* LAPB. */
```

相关声明：[ARPHRD_LAPB](#af09e5ae697b5b32f1e9d053b22a2642c)。

<a id="r_a3d7f861b4576376afe5a406179df42d8"></a>

```c
#define ARPHRD_DDCMP 517 /* Digital's DDCMP. */
```

相关声明：[ARPHRD_DDCMP](#a3d7f861b4576376afe5a406179df42d8)。

<a id="r_a67c7faf6cac1fbc281e82cae47360f30"></a>

```c
#define ARPHRD_RAWHDLC 518 /* Raw HDLC. */
```

相关声明：[ARPHRD_RAWHDLC](#a67c7faf6cac1fbc281e82cae47360f30)。

<a id="r_ab2b4f27b07b7e2d03e5873f32089dc23"></a>

```c
#define ARPHRD_RAWIP 519 /* Raw IP. */
```

相关声明：[ARPHRD_RAWIP](#ab2b4f27b07b7e2d03e5873f32089dc23)。

<a id="r_a258c6b24592ed0bfffd287bcf72184cd"></a>

```c
#define ARPHRD_TUNNEL 768 /* IPIP tunnel. */
```

相关声明：[ARPHRD_TUNNEL](#a258c6b24592ed0bfffd287bcf72184cd)。

<a id="r_a28d782f6db80ae8ada7f213842ff2869"></a>

```c
#define ARPHRD_TUNNEL6 769 /* IPIP6 tunnel. */
```

相关声明：[ARPHRD_TUNNEL6](#a28d782f6db80ae8ada7f213842ff2869)。

<a id="r_a49796245f7c1f8f4d58e5ead7af6c66d"></a>

```c
#define ARPHRD_FRAD 770 /* Frame Relay Access Device. */
```

相关声明：[ARPHRD_FRAD](#a49796245f7c1f8f4d58e5ead7af6c66d)。

<a id="r_a282f35b40f5bdb27cfa179e498934c81"></a>

```c
#define ARPHRD_SKIP 771 /* SKIP vif. */
```

相关声明：[ARPHRD_SKIP](#a282f35b40f5bdb27cfa179e498934c81)。

<a id="r_a4ee77f8d80bda9f59f5bd7163854e425"></a>

```c
#define ARPHRD_LOOPBACK 772 /* Loopback device. */
```

相关声明：[ARPHRD_LOOPBACK](#a4ee77f8d80bda9f59f5bd7163854e425)。

<a id="r_a2a6a8456b8d00c4751937f7361d77c87"></a>

```c
#define ARPHRD_LOCALTLK 773 /* Localtalk device. */
```

相关声明：[ARPHRD_LOCALTLK](#a2a6a8456b8d00c4751937f7361d77c87)。

<a id="r_a270793cc06db405a5f814e4ad8743802"></a>

```c
#define ARPHRD_FDDI 774 /* Fiber Distributed Data Interface. */
```

相关声明：[ARPHRD_FDDI](#a270793cc06db405a5f814e4ad8743802)。

<a id="r_aaa09c89bce8795a20f412e75cb441adf"></a>

```c
#define ARPHRD_BIF 775 /* AP1000 BIF. */
```

相关声明：[ARPHRD_BIF](#aaa09c89bce8795a20f412e75cb441adf)。

<a id="r_a40d57acc78d91f5f2bd6ebae7db18aeb"></a>

```c
#define ARPHRD_SIT 776 /* sit0 device - IPv6-in-IPv4. */
```

相关声明：[ARPHRD_SIT](#a40d57acc78d91f5f2bd6ebae7db18aeb)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_a47668de0966a3040187f2a640253278b"></a>

```c
#define ARPHRD_IPDDP 777 /* IP-in-DDP tunnel. */
```

相关声明：[ARPHRD_IPDDP](#a47668de0966a3040187f2a640253278b)。

<a id="r_abc6758e951b1761b8ae3748d66b8b830"></a>

```c
#define ARPHRD_IPGRE 778 /* GRE over IP. */
```

相关声明：[ARPHRD_IPGRE](#abc6758e951b1761b8ae3748d66b8b830)。

<a id="r_a90dfe4049e2164cc19bd3b54f2bd2e3f"></a>

```c
#define ARPHRD_PIMREG 779 /* PIMSM register interface. */
```

相关声明：[ARPHRD_PIMREG](#a90dfe4049e2164cc19bd3b54f2bd2e3f)。

<a id="r_a41de3e5719f2d77703b7da4dced39096"></a>

```c
#define ARPHRD_HIPPI 780 /* High Performance Parallel I'face. */
```

相关声明：[ARPHRD_HIPPI](#a41de3e5719f2d77703b7da4dced39096)。

<a id="r_acb4198100868cf41fbbce66aca49b616"></a>

```c
#define ARPHRD_ASH 781 /* (Nexus Electronics) Ash. */
```

相关声明：[ARPHRD_ASH](#acb4198100868cf41fbbce66aca49b616)。

<a id="r_a0b809ee9057fcd57da421e5e0aae06a7"></a>

```c
#define ARPHRD_ECONET 782 /* Acorn Econet. */
```

相关声明：[ARPHRD_ECONET](#a0b809ee9057fcd57da421e5e0aae06a7)。

<a id="r_a09d2e25da54b5044c67e6ea285a26728"></a>

```c
#define ARPHRD_IRDA 783 /* Linux-IrDA. */
```

相关声明：[ARPHRD_IRDA](#a09d2e25da54b5044c67e6ea285a26728)。

<a id="r_aaea9329315517c7ca86311f8644cd254"></a>

```c
#define ARPHRD_FCPP 784 /* Point to point fibrechanel. */
```

相关声明：[ARPHRD_FCPP](#aaea9329315517c7ca86311f8644cd254)。

<a id="r_ab57dbb123cafe8fab5d73fe516cbaab4"></a>

```c
#define ARPHRD_FCAL 785 /* Fibrechanel arbitrated loop. */
```

相关声明：[ARPHRD_FCAL](#ab57dbb123cafe8fab5d73fe516cbaab4)。

<a id="r_ac8dc8a30027ee7ffca6fff796ad61d56"></a>

```c
#define ARPHRD_FCPL 786 /* Fibrechanel public loop. */
```

相关声明：[ARPHRD_FCPL](#ac8dc8a30027ee7ffca6fff796ad61d56)。

<a id="r_ac1156888d5f5f118bdb6308cdb3d019f"></a>

```c
#define ARPHRD_FCFABRIC 787 /* Fibrechanel fabric. */
```

相关声明：[ARPHRD_FCFABRIC](#ac1156888d5f5f118bdb6308cdb3d019f)。

<a id="r_a00bc6b1bb5f426bb58241ba16ad870e7"></a>

```c
#define ARPHRD_IEEE802_TR 800 /* Magic type ident for TR. */
```

相关声明：[ARPHRD_IEEE802_TR](#a00bc6b1bb5f426bb58241ba16ad870e7)。

<a id="r_acc8226bf5c1c690acdeb7d827e061107"></a>

```c
#define ARPHRD_IEEE80211 801 /* IEEE 802.11. */
```

相关声明：[ARPHRD_IEEE80211](#acc8226bf5c1c690acdeb7d827e061107)。

<a id="r_a9b01c3c5cd6cce41e141cb185ffc2f65"></a>

```c
#define ARPHRD_IEEE80211_PRISM 802 /* IEEE 802.11 + Prism2 header. */
```

相关声明：[ARPHRD_IEEE80211_PRISM](#a9b01c3c5cd6cce41e141cb185ffc2f65)。

<a id="r_a7b897c5160766a1c3f1ea51635419b48"></a>

```c
#define ARPHRD_IEEE80211_RADIOTAP 803 /* IEEE 802.11 + radiotap header. */
```

相关声明：[ARPHRD_IEEE80211_RADIOTAP](#a7b897c5160766a1c3f1ea51635419b48)。

<a id="r_adff33b6bd20a8b03fedce3b7fec456e9"></a>

```c
#define ARPHRD_IEEE802154 804 /* IEEE 802.15.4 header. */
```

相关声明：[ARPHRD_IEEE802154](#adff33b6bd20a8b03fedce3b7fec456e9)。

<a id="r_a2794d558aa2c279f8ac4e3f4e11f72cd"></a>

```c
#define ARPHRD_IEEE802154_PHY 805 /* IEEE 802.15.4 PHY header. */
```

相关声明：[ARPHRD_IEEE802154_PHY](#a2794d558aa2c279f8ac4e3f4e11f72cd)。

<a id="r_a9bc958dad255bdc3fc3fbe067adaf017"></a>

```c
#define ARPHRD_VOID 0xFFFF /* Void type, nothing is known. */
```

相关声明：[ARPHRD_VOID](#a9bc958dad255bdc3fc3fbe067adaf017)。

<a id="r_af54d98448c0e1e1b02d9e565508a4280"></a>

```c
#define ARPHRD_NONE 0xFFFE /* Zero header length. */
```

相关声明：[ARPHRD_NONE](#af54d98448c0e1e1b02d9e565508a4280)。

## 142.2\_详细说明（Detailed Documentation）

<a id="a74df13d4969bcad5e7bf0db3706dc388"></a>

### `ARPHRD_ADAPT`

```c
#define ARPHRD_ADAPT 264
```

<a id="a7614228ba176316183dc2ccd61134b6a"></a>

### `ARPHRD_APPLETLK`

```c
#define ARPHRD_APPLETLK 8 /* APPLEtalk. */
```

<a id="ade606bd55e7f4f0a03278eed4a8badf8"></a>

### `ARPHRD_ARCNET`

```c
#define ARPHRD_ARCNET 7 /* ARCnet. */
```

<a id="acb4198100868cf41fbbce66aca49b616"></a>

### `ARPHRD_ASH`

```c
#define ARPHRD_ASH 781 /* (Nexus Electronics) Ash. */
```

<a id="a52fe51e586dd5952a78a42de1a2992e8"></a>

### `ARPHRD_ATM`

```c
#define ARPHRD_ATM 19 /* ATM. */
```

<a id="aeaba33578b2449674b76cd29692a687c"></a>

### `ARPHRD_AX25`

```c
#define ARPHRD_AX25 3 /* AX.25 Level 2. */
```

<a id="aaa09c89bce8795a20f412e75cb441adf"></a>

### `ARPHRD_BIF`

```c
#define ARPHRD_BIF 775 /* AP1000 BIF. */
```

<a id="a07220dd6d6e255e11f0ea1cf99feba0d"></a>

### `ARPHRD_CAN`

```c
#define ARPHRD_CAN 280 /* Controller Area Network. */
```

<a id="a6b5310b0311353a79e66f7700ce88e8d"></a>

### `ARPHRD_CHAOS`

```c
#define ARPHRD_CHAOS 5 /* Chaosnet. */
```

<a id="a410eced86d38da357b0ffb10adba4ca2"></a>

### `ARPHRD_CISCO`

```c
#define ARPHRD_CISCO 513 /* Cisco HDLC. */
```

<a id="a6651e9c8291dccd470c9426986a160ad"></a>

### `ARPHRD_CSLIP`

```c
#define ARPHRD_CSLIP 257
```

<a id="ab05b137e1709daec52097cd07d9c86c7"></a>

### `ARPHRD_CSLIP6`

```c
#define ARPHRD_CSLIP6 259
```

<a id="a3d7f861b4576376afe5a406179df42d8"></a>

### `ARPHRD_DDCMP`

```c
#define ARPHRD_DDCMP 517 /* Digital's DDCMP. */
```

<a id="af02df7fa9173bc0716fe46eb5d45c3e1"></a>

### `ARPHRD_DLCI`

```c
#define ARPHRD_DLCI 15 /* Frame Relay DLCI. */
```

<a id="a0b809ee9057fcd57da421e5e0aae06a7"></a>

### `ARPHRD_ECONET`

```c
#define ARPHRD_ECONET 782 /* Acorn Econet. */
```

<a id="aa2d3040a4ca3fa7aa832b0863bb032a4"></a>

### `ARPHRD_EETHER`

```c
#define ARPHRD_EETHER 2 /* Experimental Ethernet. */
```

<a id="a99b0f33012409144fc0b51bfa835dcba"></a>

### `ARPHRD_ETHER`

```c
#define ARPHRD_ETHER 1 /* Ethernet 10/100Mbps. */
```

<a id="abbc7280c99b6907038c8e2a433091133"></a>

### `ARPHRD_EUI64`

```c
#define ARPHRD_EUI64 27 /* EUI-64. */
```

<a id="ab57dbb123cafe8fab5d73fe516cbaab4"></a>

### `ARPHRD_FCAL`

```c
#define ARPHRD_FCAL 785 /* Fibrechanel arbitrated loop. */
```

<a id="ac1156888d5f5f118bdb6308cdb3d019f"></a>

### `ARPHRD_FCFABRIC`

```c
#define ARPHRD_FCFABRIC 787 /* Fibrechanel fabric. */
```

<a id="ac8dc8a30027ee7ffca6fff796ad61d56"></a>

### `ARPHRD_FCPL`

```c
#define ARPHRD_FCPL 786 /* Fibrechanel public loop. */
```

<a id="aaea9329315517c7ca86311f8644cd254"></a>

### `ARPHRD_FCPP`

```c
#define ARPHRD_FCPP 784 /* Point to point fibrechanel. */
```

<a id="a270793cc06db405a5f814e4ad8743802"></a>

### `ARPHRD_FDDI`

```c
#define ARPHRD_FDDI 774 /* Fiber Distributed Data Interface. */
```

<a id="a49796245f7c1f8f4d58e5ead7af6c66d"></a>

### `ARPHRD_FRAD`

```c
#define ARPHRD_FRAD 770 /* Frame Relay Access Device. */
```

<a id="a8e2c80f4cd4774f76cd7803ba31b27e1"></a>

### `ARPHRD_HDLC`

```c
#define ARPHRD_HDLC ARPHRD_CISCO
```

<a id="a41de3e5719f2d77703b7da4dced39096"></a>

### `ARPHRD_HIPPI`

```c
#define ARPHRD_HIPPI 780 /* High Performance Parallel I'face. */
```

<a id="a0eb9519f0ea218877755913bb4533091"></a>

### `ARPHRD_HWX25`

```c
#define ARPHRD_HWX25 272 /* Boards with X.25 in firmware. */
```

<a id="a4d072593e2ce7018e74f42eab74b1506"></a>

### `ARPHRD_IEEE1394`

```c
#define ARPHRD_IEEE1394 24 /* IEEE 1394 IPv4 - RFC 2734. */
```

<a id="a63153ce22626e108b5046b89d918803f"></a>

### `ARPHRD_IEEE802`

```c
#define ARPHRD_IEEE802 6 /* IEEE 802.2 Ethernet/TR/TB. */
```

<a id="acc8226bf5c1c690acdeb7d827e061107"></a>

### `ARPHRD_IEEE80211`

```c
#define ARPHRD_IEEE80211 801 /* IEEE 802.11. */
```

<a id="a9b01c3c5cd6cce41e141cb185ffc2f65"></a>

### `ARPHRD_IEEE80211_PRISM`

```c
#define ARPHRD_IEEE80211_PRISM 802 /* IEEE 802.11 + Prism2 header. */
```

<a id="a7b897c5160766a1c3f1ea51635419b48"></a>

### `ARPHRD_IEEE80211_RADIOTAP`

```c
#define ARPHRD_IEEE80211_RADIOTAP 803 /* IEEE 802.11 + radiotap header. */
```

<a id="adff33b6bd20a8b03fedce3b7fec456e9"></a>

### `ARPHRD_IEEE802154`

```c
#define ARPHRD_IEEE802154 804 /* IEEE 802.15.4 header. */
```

<a id="a2794d558aa2c279f8ac4e3f4e11f72cd"></a>

### `ARPHRD_IEEE802154_PHY`

```c
#define ARPHRD_IEEE802154_PHY 805 /* IEEE 802.15.4 PHY header. */
```

<a id="a00bc6b1bb5f426bb58241ba16ad870e7"></a>

### `ARPHRD_IEEE802_TR`

```c
#define ARPHRD_IEEE802_TR 800 /* Magic type ident for TR. */
```

<a id="abb8ca5a62f0f53187a295f0e96ba208b"></a>

### `ARPHRD_INFINIBAND`

```c
#define ARPHRD_INFINIBAND 32 /* InfiniBand. */
```

<a id="a47668de0966a3040187f2a640253278b"></a>

### `ARPHRD_IPDDP`

```c
#define ARPHRD_IPDDP 777 /* IP-in-DDP tunnel. */
```

<a id="abc6758e951b1761b8ae3748d66b8b830"></a>

### `ARPHRD_IPGRE`

```c
#define ARPHRD_IPGRE 778 /* GRE over IP. */
```

<a id="a09d2e25da54b5044c67e6ea285a26728"></a>

### `ARPHRD_IRDA`

```c
#define ARPHRD_IRDA 783 /* Linux-IrDA. */
```

<a id="af09e5ae697b5b32f1e9d053b22a2642c"></a>

### `ARPHRD_LAPB`

```c
#define ARPHRD_LAPB 516 /* LAPB. */
```

<a id="a2a6a8456b8d00c4751937f7361d77c87"></a>

### `ARPHRD_LOCALTLK`

```c
#define ARPHRD_LOCALTLK 773 /* Localtalk device. */
```

<a id="a4ee77f8d80bda9f59f5bd7163854e425"></a>

### `ARPHRD_LOOPBACK`

```c
#define ARPHRD_LOOPBACK 772 /* Loopback device. */
```

<a id="ab490545ded34d438fe2fcc1eaaa39c1e"></a>

### `ARPHRD_MCTP`

```c
#define ARPHRD_MCTP 290
```

<a id="ad597c946041d8b4d02b41c3b2145e10a"></a>

### `ARPHRD_METRICOM`

```c
#define ARPHRD_METRICOM 23 /* Metricom STRIP (new IANA id). */
```

<a id="ae1acb8a91a94d38dd411fb5e719f35b0"></a>

### `ARPHRD_NETROM`

```c
#define ARPHRD_NETROM 0 /* From KA9Q: NET/ROM pseudo. */
```

<a id="af54d98448c0e1e1b02d9e565508a4280"></a>

### `ARPHRD_NONE`

```c
#define ARPHRD_NONE 0xFFFE /* Zero header length. */
```

<a id="a90dfe4049e2164cc19bd3b54f2bd2e3f"></a>

### `ARPHRD_PIMREG`

```c
#define ARPHRD_PIMREG 779 /* PIMSM register interface. */
```

<a id="a18dec8be041946b4a3a75ec73bb4293c"></a>

### `ARPHRD_PPP`

```c
#define ARPHRD_PPP 512
```

<a id="a394dfc37c8b6c429af9d6562a76b0c99"></a>

### `ARPHRD_PRONET`

```c
#define ARPHRD_PRONET 4 /* PROnet token ring. */
```

<a id="a67c7faf6cac1fbc281e82cae47360f30"></a>

### `ARPHRD_RAWHDLC`

```c
#define ARPHRD_RAWHDLC 518 /* Raw HDLC. */
```

<a id="ab2b4f27b07b7e2d03e5873f32089dc23"></a>

### `ARPHRD_RAWIP`

```c
#define ARPHRD_RAWIP 519 /* Raw IP. */
```

<a id="aea2aa154ca4cc488c86727dc44b36b19"></a>

### `ARPHRD_ROSE`

```c
#define ARPHRD_ROSE 270
```

<a id="af34e0978e6bb11cf230b5b691a5a1b8a"></a>

### `ARPHRD_RSRVD`

```c
#define ARPHRD_RSRVD 260 /* Notional KISS type. */
```

<a id="a40d57acc78d91f5f2bd6ebae7db18aeb"></a>

### `ARPHRD_SIT`

```c
#define ARPHRD_SIT 776 /* sit0 device - IPv6-in-IPv4. */
```

<a id="a282f35b40f5bdb27cfa179e498934c81"></a>

### `ARPHRD_SKIP`

```c
#define ARPHRD_SKIP 771 /* SKIP vif. */
```

<a id="a45d939a8b7cfeb1145cc5a49f6d2a399"></a>

### `ARPHRD_SLIP`

```c
#define ARPHRD_SLIP 256
```

<a id="ae35c4cbe46fc19d363a7af42c6dcf273"></a>

### `ARPHRD_SLIP6`

```c
#define ARPHRD_SLIP6 258
```

<a id="a258c6b24592ed0bfffd287bcf72184cd"></a>

### `ARPHRD_TUNNEL`

```c
#define ARPHRD_TUNNEL 768 /* IPIP tunnel. */
```

<a id="a28d782f6db80ae8ada7f213842ff2869"></a>

### `ARPHRD_TUNNEL6`

```c
#define ARPHRD_TUNNEL6 769 /* IPIP6 tunnel. */
```

<a id="a9bc958dad255bdc3fc3fbe067adaf017"></a>

### `ARPHRD_VOID`

```c
#define ARPHRD_VOID 0xFFFF /* Void type, nothing is known. */
```

<a id="a1faa7cf295013abcee809dc908d9be6b"></a>

### `ARPHRD_X25`

```c
#define ARPHRD_X25 271 /* CCITT X.25. */
```


## 142.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/if__arp_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P141_zephyr__posix__net__if.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P143_zephyr__dt-bindings__clock__ifx_clock_source_boards.h_文件参考.md)
