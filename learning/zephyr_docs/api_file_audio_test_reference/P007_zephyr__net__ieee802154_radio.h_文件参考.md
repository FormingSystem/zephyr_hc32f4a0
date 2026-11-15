---
id: learning.zephyr-docs.api-file-audio-test-reference.page-7
title: zephyr__net__ieee802154_radio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_net\_\_ieee802154\_radio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IEEE 802.15.4的公共驱动API（Driver API）。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_pkt.h>
#include <zephyr/net/net_time.h>
#include <zephyr/net/ieee802154.h>
#include <zephyr/net/ieee802154_ie.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

IEEE 802.15.4 公共驱动 API（Driver API）。注意（Note）：本文件对该标准的所有引用均指向 IEEE 802.15.4-2020。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_ieee802154_5Fphy_5Fchannel_5Frange"></a>

```c
struct ieee802154_phy_channel_range
```

相关声明：[ieee802154_phy_channel_range](../network_core_model_reference/P039_ieee802154_phy_channel_range_结构体.md)。

表示一个受支持的信道范围（Channel Range），见ieee802154_phy_supported_channels。

<a id="r_ieee802154_5Fphy_5Fsupported_5Fchannels"></a>

```c
struct ieee802154_phy_supported_channels
```

相关声明：[ieee802154_phy_supported_channels](../network_core_model_reference/P040_ieee802154_phy_supported_channels_结构体.md)。

表示驱动对给定接口支持的信道列表，见IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_RANGES。

<a id="r_ieee802154_5Ffilter"></a>

```c
struct ieee802154_filter
```

相关声明：[ieee802154_filter](../network_core_model_reference/P017_ieee802154_filter_结构体.md)。

过滤器值（Filter Value），见ieee802154_radio_api::filter。

<a id="r_ieee802154_5Fkey"></a>

```c
struct ieee802154_key
```

相关声明：[ieee802154_key](../network_core_model_reference/P032_ieee802154_key_结构体.md)。

发送安全卸载（Transmit Security Offloading）的密钥配置，见IEEE802154_CONFIG_MAC_KEYS。

<a id="r_ieee802154_5Fconfig"></a>

```c
struct ieee802154_config
```

相关声明：[ieee802154_config](../network_core_model_reference/P014_ieee802154_config_结构体.md)。

IEEE 802.15.4驱动的配置数据（Configuration Data）。

<a id="r_ieee802154_5Fattr_5Fvalue"></a>

```c
struct ieee802154_attr_value
```

相关声明：[ieee802154_attr_value](../network_core_model_reference/P005_ieee802154_attr_value_结构体.md)。

IEEE 802.15.4驱动的属性值（Attribute Values）。

<a id="r_ieee802154_5Fradio_5Fapi"></a>

```c
struct ieee802154_radio_api
```

相关声明：[ieee802154_radio_api](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md)。

IEEE 802.15.4驱动的接口API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="define-members-0"></a>

### IEEE 802.15.4-2020 第 6 节：MAC 功能说明（MAC Functional Description）

<a id="r_gaf228d9c26cedd5c790b7ebae41b5f937"></a>

```c
#define IEEE802154_PHY_SYMBOLS_PER_SECOND(symbol_period_ns)
```

相关声明：[IEEE802154_PHY_SYMBOLS_PER_SECOND](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf228d9c26cedd5c790b7ebae41b5f937)。

符号周期（Symbol Period），以及由此决定的符号率（Symbol Rate），定义于第 6.1 节：“MAC 定义中的某些时序参数以 PHY 符号为单位。

<a id="define-members-1"></a>

### IEEE 802.15.4-2020 第 8 节：MAC 服务（MAC Services）

<a id="r_gadb590005c9120e6b04aa430ebb306b8f"></a>

```c
#define IEEE802154_MAC_A_BASE_SLOT_DURATION 60U
```

相关声明：[IEEE802154_MAC_A_BASE_SLOT_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gadb590005c9120e6b04aa430ebb306b8f)。

超帧阶数（Superframe Order）为 0 时，构成一个超帧时隙（Superframe Slot）的 PHY 符号数；参见第 8.4.2 节表 8-93 的 aBaseSlotDuration，以及第 6.2.1 节。

<a id="r_ga662c1add47deb9807e848aeeee5e6842"></a>

```c
#define IEEE802154_MAC_A_NUM_SUPERFRAME_SLOTS 16U
```

相关声明：[IEEE802154_MAC_A_NUM_SUPERFRAME_SLOTS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga662c1add47deb9807e848aeeee5e6842)。

任意超帧（Superframe）包含的时隙数量；参见第 8.4.2 节表 8-93 的 aNumSuperframeSlots。

<a id="r_ga52358c63c386b72f190d3b487c9ba286"></a>

```c
#define IEEE802154_MAC_A_BASE_SUPERFRAME_DURATION (IEEE802154_MAC_A_BASE_SLOT_DURATION * IEEE802154_MAC_A_NUM_SUPERFRAME_SLOTS)
```

相关声明：[IEEE802154_MAC_A_BASE_SUPERFRAME_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga52358c63c386b72f190d3b487c9ba286)、[IEEE802154_MAC_A_BASE_SLOT_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gadb590005c9120e6b04aa430ebb306b8f)、[IEEE802154_MAC_A_NUM_SUPERFRAME_SLOTS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga662c1add47deb9807e848aeeee5e6842)。

超帧阶数（Superframe Order）为 0 时，构成一个超帧（Superframe）的 PHY 符号数；参见第 8.4.2 节表 8-93 的 aBaseSuperframeDuration。

<a id="r_ga86f3186304b02de3096d521238d407db"></a>

```c
#define IEEE802154_MAC_A_UNIT_BACKOFF_PERIOD(turnaround_time)
```

相关声明：[IEEE802154_MAC_A_UNIT_BACKOFF_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga86f3186304b02de3096d521238d407db)。

MAC PIB 属性 aUnitBackoffPeriod，参见第 8.4.2 节表 8-93，以符号周期（Symbol Periods）为单位，适用于除 920 MHz 频段 SUN PHY 以外的所有 PHY。

<a id="r_ga132be1037c5db1311c6d0c7d74e1fe40"></a>

```c
#define IEEE802154_MAC_RESPONSE_WAIT_TIME_DEFAULT 32U
```

相关声明：[IEEE802154_MAC_RESPONSE_WAIT_TIME_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga132be1037c5db1311c6d0c7d74e1fe40)。

默认 macResponseWaitTime，以 aBaseSuperframeDuration 的倍数表示，定义于第 8.4.3.1 节表 8-94。

<a id="define-members-2"></a>

### IEEE 802.15.4-2020 第 11 节：物理层服务（PHY Services）

<a id="r_ga9e95bf5d8ddb1087cdd9eb2aa80d100e"></a>

```c
#define IEEE802154_PHY_A_TURNAROUND_TIME_DEFAULT 12U
```

相关声明：[IEEE802154_PHY_A_TURNAROUND_TIME_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga9e95bf5d8ddb1087cdd9eb2aa80d100e)。

默认 PHY PIB 属性 aTurnaroundTime，以 PHY 符号（Symbols）为单位；参见第 11.3 节表 11-1。

<a id="r_ga68115b80097b116b704431808469450b"></a>

```c
#define IEEE802154_PHY_A_TURNAROUND_TIME_1MS(symbol_period_ns)
```

相关声明：[IEEE802154_PHY_A_TURNAROUND_TIME_1MS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga68115b80097b116b704431808469450b)。

SUN、RS-GFSK、TVWS 和 LECIM FSK PHY 的 PHY PIB 属性 aTurnaroundTime，以 PHY 符号（Symbols）为单位；参见第 11.3 节表 11-1。

<a id="r_gaf58b5d421167c2075dcdfdbaba5956dd"></a>

```c
#define IEEE802154_PHY_A_CCA_TIME 8U
```

相关声明：[IEEE802154_PHY_A_CCA_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf58b5d421167c2075dcdfdbaba5956dd)。

PHY PIB 属性 aCcaTime，以 PHY 符号（Symbols）为单位，适用于除 SUN O-QPSK 以外的所有 PHY；参见第 11.3 节表 11-1。

<a id="define-members-3"></a>

### IEEE 802.15.4-2020 第 12 节：O-QPSK 物理层（PHY）

<a id="r_ga32ce931f3d35d779e4251c37f61583f5"></a>

```c
#define IEEE802154_PHY_OQPSK_868MHZ_SYMBOL_PERIOD_NS 40000LL
```

相关声明：[IEEE802154_PHY_OQPSK_868MHZ_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga32ce931f3d35d779e4251c37f61583f5)。

O-QPSK 868 MHz 频段的符号周期（Symbol Period），参见第 12.3.3 节。

<a id="r_gaff3d58945d53e824f1fb1ca11dd9997b"></a>

```c
#define IEEE802154_PHY_OQPSK_780_TO_2450MHZ_SYMBOL_PERIOD_NS 16000LL
```

相关声明：[IEEE802154_PHY_OQPSK_780_TO_2450MHZ_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaff3d58945d53e824f1fb1ca11dd9997b)。

O-QPSK 780 MHz、915 MHz、2380 MHz 和 2450 MHz 频段的符号周期（Symbol Period），参见第 12.3.3 节。

<a id="define-members-4"></a>

### IEEE 802.15.4-2020 第 13 节：BPSK 物理层（PHY）

<a id="r_ga1dc4319d0a8d979c7455e1f71f45d885"></a>

```c
#define IEEE802154_PHY_BPSK_868MHZ_SYMBOL_PERIOD_NS 50000LL
```

相关声明：[IEEE802154_PHY_BPSK_868MHZ_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga1dc4319d0a8d979c7455e1f71f45d885)。

BPSK 868 MHz 频段的符号周期（Symbol Period），参见第 13.3.3 节。

<a id="r_gaa12344b6a118995b63c5bd4bc3180efd"></a>

```c
#define IEEE802154_PHY_BPSK_915MHZ_SYMBOL_PERIOD_NS 25000LL
```

相关声明：[IEEE802154_PHY_BPSK_915MHZ_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaa12344b6a118995b63c5bd4bc3180efd)。

BPSK 915 MHz 频段的符号周期（Symbol Period），参见第 13.3.3 节。

<a id="define-members-5"></a>

### IEEE 802.15.4-2020 第 19 节：SUN FSK 物理层（PHY）

<a id="r_ga155b5b5a06311c1bde3f36e06d02ed7d"></a>

```c
#define IEEE802154_PHY_SUN_FSK_863MHZ_915MHZ_SYMBOL_PERIOD_NS 20000LL
```

相关声明：[IEEE802154_PHY_SUN_FSK_863MHZ_915MHZ_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga155b5b5a06311c1bde3f36e06d02ed7d)。

SUN FSK 863 MHz 和 915 MHz 频段的符号周期（Symbol Periods），参见第 19.1 节表 19-1。

<a id="r_gac088ee6d01014a12169e74111ea61993"></a>

```c
#define IEEE802154_PHY_SUN_FSK_PHR_LEN 2
```

相关声明：[IEEE802154_PHY_SUN_FSK_PHR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gac088ee6d01014a12169e74111ea61993)。

SUN FSK PHY 头部长度（Header Length），单位为字节；参见第 19.2.4 节。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.3\_函数（Functions）

<a id="func-members-0"></a>

### IEEE 802.15.4 驱动辅助接口（Driver Utils）

<a id="r_gaf5d7bdde2a9774f9d90604a6e203bb07"></a>

```c
static bool ieee802154_is_ar_flag_set (struct net_buf *frag)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[ieee802154_is_ar_flag_set](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf5d7bdde2a9774f9d90604a6e203bb07)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

检查给定网络数据包库（Network Packet Library）对象内的帧是否设置了确认请求标志（AR Flag）。

<a id="func-members-1"></a>

### IEEE 802.15.4 驱动回调（Driver Callbacks）

<a id="r_ga68e1f89571ccbefef61a5496577337fc"></a>

```c
enum net_verdict ieee802154_handle_ack (struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)、[ieee802154_handle_ack](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga68e1f89571ccbefef61a5496577337fc)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

IEEE 802.15.4 驱动调用二层（L2）的确认处理回调（ACK Handling Callback）；驱动收到 ACK 数据包时必须调用它。

<a id="r_gad2a4cb5df84ffe20b83fc54dc9bcfc91"></a>

```c
void ieee802154_init (struct net_if *iface)
```

相关声明：[ieee802154_init](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gad2a4cb5df84ffe20b83fc54dc9bcfc91)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

IEEE 802.15.4 驱动调用二层（L2）的初始化回调（Initialization Callback），用于初始化给定接口当前使用的 L2 协议栈。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 7.4\_IEEE 802.15.4-2020 第 10 节：通用物理层要求（General PHY Requirements）

<a id="r_ga78d4df389a7bd11c55e5c7b683897a9b"></a>

```c
#define IEEE802154_DEFINE_PHY_SUPPORTED_CHANNELS(drv_attr, from, to)
```

相关声明：[IEEE802154_DEFINE_PHY_SUPPORTED_CHANNELS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga78d4df389a7bd11c55e5c7b683897a9b)。

为支持的信道驱动属性（Supported Channels Driver Attribute）分配内存，其单一信道范围在所有驱动实例间保持不变。

<a id="r_gacabc7386bea701373dfb36ab65bd36a9"></a>

```c
enum ieee802154_phy_channel_page { IEEE802154_ATTR_PHY_CHANNEL_PAGE_ZERO_OQPSK_2450_BPSK_868_915 = BIT(0) , IEEE802154_ATTR_PHY_CHANNEL_PAGE_ONE_DEPRECATED = BIT(1) , IEEE802154_ATTR_PHY_CHANNEL_PAGE_TWO_OQPSK_868_915 = BIT(2) , IEEE802154_ATTR_PHY_CHANNEL_PAGE_THREE_CSS = BIT(3) , IEEE802154_ATTR_PHY_CHANNEL_PAGE_FOUR_HRP_UWB = BIT(4) , IEEE802154_ATTR_PHY_CHANNEL_PAGE_FIVE_OQPSK_780 = BIT(5) , IEEE802154_ATTR_PHY_CHANNEL_PAGE_SIX_RESERVED = BIT(6) , IEEE802154_ATTR_PHY_CHANNEL_PAGE_SEVEN_MSK = BIT(7) , IEEE802154_ATTR_PHY_CHANNEL_PAGE_EIGHT_LRP_UWB = BIT(8) , IEEE802154_ATTR_PHY_CHANNEL_PAGE_NINE_SUN_PREDEFINED = BIT(9) , IEEE802154_ATTR_PHY_CHANNEL_PAGE_TEN_SUN_FSK_GENERIC = BIT(10) , IEEE802154_ATTR_PHY_CHANNEL_PAGE_ELEVEN_OQPSK_2380 = BIT(11) , IEEE802154_ATTR_PHY_CHANNEL_PAGE_TWELVE_LECIM = BIT(12) , IEEE802154_ATTR_PHY_CHANNEL_PAGE_THIRTEEN_RCC = BIT(13) }
```

相关声明：[ieee802154_phy_channel_page](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gacabc7386bea701373dfb36ab65bd36a9)、[IEEE802154_ATTR_PHY_CHANNEL_PAGE_ZERO_OQPSK_2450_BPSK_868_915](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a72b17a977aeb6792f7d2016117f4b2f9)、[IEEE802154_ATTR_PHY_CHANNEL_PAGE_ONE_DEPRECATED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a371a12ec5d762b03058fb2532fa04e45)、[IEEE802154_ATTR_PHY_CHANNEL_PAGE_TWO_OQPSK_868_915](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a5776e0160927b83f4e4e8d6479aaf804)、[IEEE802154_ATTR_PHY_CHANNEL_PAGE_THREE_CSS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a6f71c162be118b0c2edce139753c867e)、[IEEE802154_ATTR_PHY_CHANNEL_PAGE_FOUR_HRP_UWB](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a68b93381ddc1184ff0ed13456cf4b6a8)、[IEEE802154_ATTR_PHY_CHANNEL_PAGE_FIVE_OQPSK_780](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a6ea456573a6ff8aed348a9dc547b2db7)、[IEEE802154_ATTR_PHY_CHANNEL_PAGE_SIX_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9ac13dda08becd3d4799d45ef02f774cc1)、[IEEE802154_ATTR_PHY_CHANNEL_PAGE_SEVEN_MSK](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a1f33467ec7659ef411b08f7a23663311)、[IEEE802154_ATTR_PHY_CHANNEL_PAGE_EIGHT_LRP_UWB](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9aa0ab080c8cdac42dbf80622d075854dc)、[IEEE802154_ATTR_PHY_CHANNEL_PAGE_NINE_SUN_PREDEFINED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a996b529c9c277d6d653d0e0ffb8b2902)、[IEEE802154_ATTR_PHY_CHANNEL_PAGE_TEN_SUN_FSK_GENERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a02a17ea787e99528b2a6a8f5107f2544)、[IEEE802154_ATTR_PHY_CHANNEL_PAGE_ELEVEN_OQPSK_2380](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9aad0644244fb5b6cba5a295e246722e94)、[IEEE802154_ATTR_PHY_CHANNEL_PAGE_TWELVE_LECIM](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a6d4023088a3607c072acebd3940340c7)、[IEEE802154_ATTR_PHY_CHANNEL_PAGE_THIRTEEN_RCC](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a56dd4ae42595ef0edb109c729e333b08)。

PHY 信道页（Channel Pages），参见第 10.1.3 节。

## 7.5\_IEEE 802.15.4-2020 第 15 节：HRP UWB 物理层（PHY）

对于 HRP UWB，符号周期（Symbol Period）由前导码符号周期（Preamble Symbol Period，T_psym）推导；参见第 11.3 节表 11-1 和第 15.2.5 节表 15-4，IEEE 802.15.4z 第 15.1 节也确认了这一点。不能仅依据信道页（Channel Page）和信道（Channel）在这些周期之间进行选择，还必须知道平均脉冲重复频率（Mean Pulse Repetition Frequency）。参见 MCPS-DATA.request 原语的 UwbPrf 参数，即第 8.3.2 节表 8-88，以及 HRP-ERDEV 长度为 91 的码的前导码参数，即 IEEE 802.15.4z 第 15.2.6.2 节表 15-7b。

<a id="r_gabeb8a359ce54618aa7df3ee8f6a434bb"></a>

```c
#define IEEE802154_PHY_HRP_UWB_PRF4_TPSYM_SYMBOL_PERIOD_NS 3974.36F
```

相关声明：[IEEE802154_PHY_HRP_UWB_PRF4_TPSYM_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gabeb8a359ce54618aa7df3ee8f6a434bb)。

标称脉冲重复频率（PRF）为 4 MHz 时的符号周期（Symbol Period）。

<a id="r_ga0123679fba7ca668aa158813f1bf2302"></a>

```c
#define IEEE802154_PHY_HRP_UWB_PRF16_TPSYM_SYMBOL_PERIOD_NS 993.59F
```

相关声明：[IEEE802154_PHY_HRP_UWB_PRF16_TPSYM_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga0123679fba7ca668aa158813f1bf2302)。

标称脉冲重复频率（PRF）为 16 MHz 时的符号周期（Symbol Period）。

<a id="r_ga59f8ba8a01171c56da6f7ae7f8983bf7"></a>

```c
#define IEEE802154_PHY_HRP_UWB_PRF64_TPSYM_SYMBOL_PERIOD_NS 1017.63F
```

相关声明：[IEEE802154_PHY_HRP_UWB_PRF64_TPSYM_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga59f8ba8a01171c56da6f7ae7f8983bf7)。

标称脉冲重复频率（PRF）为 64 MHz 时的符号周期（Symbol Period）。

<a id="r_gaa25ba5b644e58cfc7de5ba5aa526ea71"></a>

```c
#define IEEE802154_PHY_HRP_UWB_ERDEV_TPSYM_SYMBOL_PERIOD_NS 729.17F
```

相关声明：[IEEE802154_PHY_HRP_UWB_ERDEV_TPSYM_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaa25ba5b644e58cfc7de5ba5aa526ea71)。

ERDEV 符号周期（Symbol Period）。

<a id="r_gacfd2faf2c3072f8851abd74fe5148ec5"></a>

```c
#define IEEE802154_PHY_HRP_UWB_RDEV
```

相关声明：[IEEE802154_PHY_HRP_UWB_RDEV](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gacfd2faf2c3072f8851abd74fe5148ec5)。

RDEV 设备掩码（Device Mask）。

<a id="r_gae02b981a3908b05b4bc0b7a2844c27c7"></a>

```c
#define IEEE802154_PHY_HRP_UWB_ERDEV
```

相关声明：[IEEE802154_PHY_HRP_UWB_ERDEV](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gae02b981a3908b05b4bc0b7a2844c27c7)。

ERDEV 设备掩码（Device Mask）。

<a id="r_ga13610aeef06372bc47d84464537fdded"></a>

```c
enum ieee802154_phy_hrp_uwb_nominal_prf { IEEE802154_PHY_HRP_UWB_PRF_OFF = 0 , IEEE802154_PHY_HRP_UWB_NOMINAL_4_M = BIT(0) , IEEE802154_PHY_HRP_UWB_NOMINAL_16_M = BIT(1) , IEEE802154_PHY_HRP_UWB_NOMINAL_64_M = BIT(2) , IEEE802154_PHY_HRP_UWB_NOMINAL_64_M_BPRF = BIT(3) , IEEE802154_PHY_HRP_UWB_NOMINAL_128_M_HPRF = BIT(4) , IEEE802154_PHY_HRP_UWB_NOMINAL_256_M_HPRF = BIT(5) }
```

相关声明：[ieee802154_phy_hrp_uwb_nominal_prf](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga13610aeef06372bc47d84464537fdded)、[IEEE802154_PHY_HRP_UWB_PRF_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddeda4369c745ed378d8273a1014322f3029a)、[IEEE802154_PHY_HRP_UWB_NOMINAL_4_M](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddeda9dc3c58366502aeab04a208937536369)、[IEEE802154_PHY_HRP_UWB_NOMINAL_16_M](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddedadf9230e6ef62ce66129bfe24f537c88a)、[IEEE802154_PHY_HRP_UWB_NOMINAL_64_M](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddeda2b24236d3531cab7d21673d065b7c29e)、[IEEE802154_PHY_HRP_UWB_NOMINAL_64_M_BPRF](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddedad920ae285cdcc2a4d59f7c23e29dce27)、[IEEE802154_PHY_HRP_UWB_NOMINAL_128_M_HPRF](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddedae6c88efd301a449b1a31e8aedf4e30ca)、[IEEE802154_PHY_HRP_UWB_NOMINAL_256_M_HPRF](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddedacb66442cf2a5e4c539b6b7edf8419be1)。

表示高脉冲重复频率超宽带物理层（HRP UWB PHY）的标称脉冲重复频率。

## 7.6\_IEEE 802.15.4 驱动 API（Driver API）

<a id="r_gaf143a9f110a2eb6b21104af6927159bc"></a>

```c
#define IEEE802154_HW_CAPS_BITS_COMMON_COUNT (13)
```

相关声明：[IEEE802154_HW_CAPS_BITS_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf143a9f110a2eb6b21104af6927159bc)。

ieee802154_hw_caps 类型使用的位数。

<a id="r_ga40912ccb268768b4e96ce9cad35476af"></a>

```c
#define IEEE802154_HW_CAPS_BITS_PRIV_START IEEE802154_HW_CAPS_BITS_COMMON_COUNT
```

相关声明：[IEEE802154_HW_CAPS_BITS_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga40912ccb268768b4e96ce9cad35476af)、[IEEE802154_HW_CAPS_BITS_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf143a9f110a2eb6b21104af6927159bc)。

此值及更高的值专用于协议或驱动专用扩展（Protocol-/Driver-specific Extensions）。

<a id="r_ga1cb6434a3a7555fe9d35c73b698cbf10"></a>

```c
#define IEEE802154_CONFIG_RX_SLOT_NONE -1LL
```

相关声明：[IEEE802154_CONFIG_RX_SLOT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga1cb6434a3a7555fe9d35c73b698cbf10)。

配置接收时隙（RX Slot）时，将 start 参数设置为此值，会取消并删除先前配置的任何接收时隙。

<a id="r_ga3828a2d56a39de92c2fd79caaac4c800"></a>

```c
#define IEEE802154_CONFIG_RX_SLOT_OFF 0LL
```

相关声明：[IEEE802154_CONFIG_RX_SLOT_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga3828a2d56a39de92c2fd79caaac4c800)。

驱动处于停用状态（Down）时，使用此 start 参数配置接收时隙（RX Slot），会在驱动启动时保持接收（RX）关闭。

<a id="r_gaf99cda89c29df3c0088fc57ec09cbcd4"></a>

```c
enum ieee802154_hw_caps { IEEE802154_HW_ENERGY_SCAN = BIT(0) , IEEE802154_HW_FCS = BIT(1) , IEEE802154_HW_FILTER = BIT(2) , IEEE802154_HW_PROMISC = BIT(3) , IEEE802154_HW_CSMA = BIT(4) , IEEE802154_HW_TX_RX_ACK = BIT(5) , IEEE802154_HW_RETRANSMISSION = BIT(6) , IEEE802154_HW_RX_TX_ACK = BIT(7) , IEEE802154_HW_TXTIME = BIT(8) , IEEE802154_HW_RXTIME = BIT(9) , IEEE802154_HW_TX_SEC = BIT(10) , IEEE802154_RX_ON_WHEN_IDLE = BIT(11) , IEEE802154_HW_SELECTIVE_TXCHANNEL = BIT(12) }
```

相关声明：[ieee802154_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf99cda89c29df3c0088fc57ec09cbcd4)、[IEEE802154_HW_ENERGY_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a179ad073a5bd34e4e4af587d07ca3f73)、[IEEE802154_HW_FCS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a0ea21cab335dd9082feb2d08be0eb5fa)、[IEEE802154_HW_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4afd09f329a708d00f1384a50c59ddde27)、[IEEE802154_HW_PROMISC](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a4adb33f2ca81a24244dead6b379cd916)、[IEEE802154_HW_CSMA](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a2ee53f11e1ed6853e1f5d9dfe7d7bdf7)、[IEEE802154_HW_TX_RX_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4ab383a932c0ac9deece68f02210089119)、[IEEE802154_HW_RETRANSMISSION](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a752472a994bdcbdf9cdf86deb0231849)、[IEEE802154_HW_RX_TX_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4aec16c4d418117de2d106e84297568b03)、[IEEE802154_HW_TXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a435d032f42d509bd78a992de6e4d7b1d)、[IEEE802154_HW_RXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a68ae68c83a87f0efc25f74edd80c4600)、[IEEE802154_HW_TX_SEC](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a7924c3d5bfe6dceeb2e8caa6df7edecb)、[IEEE802154_RX_ON_WHEN_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4ac1e00966043e5884c4cbd65fb26f0c0b)、[IEEE802154_HW_SELECTIVE_TXCHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4ab6cf4f3552d6193027a538a13b95952e)。

IEEE 802.15.4 驱动能力（Driver Capabilities）。

<a id="r_gaa1971591e72866d0f3f0d4db2931e25a"></a>

```c
enum ieee802154_filter_type { IEEE802154_FILTER_TYPE_IEEE_ADDR , IEEE802154_FILTER_TYPE_SHORT_ADDR , IEEE802154_FILTER_TYPE_PAN_ID , IEEE802154_FILTER_TYPE_SRC_IEEE_ADDR , IEEE802154_FILTER_TYPE_SRC_SHORT_ADDR }
```

相关声明：[ieee802154_filter_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaa1971591e72866d0f3f0d4db2931e25a)、[IEEE802154_FILTER_TYPE_IEEE_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaa1971591e72866d0f3f0d4db2931e25aa928a93b536c6408b3d77aa329c274fe8)、[IEEE802154_FILTER_TYPE_SHORT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaa1971591e72866d0f3f0d4db2931e25aa2fa1ac98a3b870fcf6e85e7ec82cfbe9)、[IEEE802154_FILTER_TYPE_PAN_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaa1971591e72866d0f3f0d4db2931e25aab44cc830999926a5d232aedabef52653)、[IEEE802154_FILTER_TYPE_SRC_IEEE_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaa1971591e72866d0f3f0d4db2931e25aade18e03611339f5f7ec4fdcdee409c21)、[IEEE802154_FILTER_TYPE_SRC_SHORT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaa1971591e72866d0f3f0d4db2931e25aac6dbb68674e7594fd4cd69bbe4ea60de)。

过滤器类型（Filter Type），参见 ieee802154_radio_api::filter。

<a id="r_ga3491982b677941442d904ce69fce7c5e"></a>

```c
enum ieee802154_event { IEEE802154_EVENT_TX_STARTED , IEEE802154_EVENT_RX_FAILED , IEEE802154_EVENT_RX_OFF }
```

相关声明：[ieee802154_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga3491982b677941442d904ce69fce7c5e)、[IEEE802154_EVENT_TX_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga3491982b677941442d904ce69fce7c5eaacd61f4466f1ef926adc9e1afe6c1648)、[IEEE802154_EVENT_RX_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga3491982b677941442d904ce69fce7c5eaef51197ca09befaee8cdfa2cde107273)、[IEEE802154_EVENT_RX_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga3491982b677941442d904ce69fce7c5eaf7ed46b9d13a232a2ea6b650514eea3d)。

驱动事件（Driver Events），参见 IEEE802154_CONFIG_EVENT_HANDLER。

<a id="r_ga04febbd15f9e6f6540d711ada5a4a1c8"></a>

```c
enum ieee802154_rx_fail_reason { IEEE802154_RX_FAIL_NOT_RECEIVED , IEEE802154_RX_FAIL_INVALID_FCS , IEEE802154_RX_FAIL_ADDR_FILTERED , IEEE802154_RX_FAIL_NO_BUFS , IEEE802154_RX_FAIL_ABORT , IEEE802154_RX_FAIL_OTHER }
```

相关声明：[ieee802154_rx_fail_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga04febbd15f9e6f6540d711ada5a4a1c8)、[IEEE802154_RX_FAIL_NOT_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8ad584824b4813626d04a85499371b9c32)、[IEEE802154_RX_FAIL_INVALID_FCS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8a103f6683ff71f4f7248ee1a0d09d6be4)、[IEEE802154_RX_FAIL_ADDR_FILTERED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8a7ff9cfcc5e4dfc2bf7abe1860a39410f)、[IEEE802154_RX_FAIL_NO_BUFS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8a7e180466cd23edf5f030c3fbefadf2d1)、[IEEE802154_RX_FAIL_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8a7bd7daaf3823d86ed48782138b671e57)、[IEEE802154_RX_FAIL_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8a5baa9dd683a717f7fbdfc5ab85935a3b)。

接收失败事件原因（RX Failed Event Reasons），参见 IEEE802154_EVENT_RX_FAILED。

<a id="r_gab2bee8752291e082cb277145cef1225d"></a>

```c
enum ieee802154_tx_mode { IEEE802154_TX_MODE_DIRECT , IEEE802154_TX_MODE_CCA , IEEE802154_TX_MODE_CSMA_CA , IEEE802154_TX_MODE_TXTIME , IEEE802154_TX_MODE_TXTIME_CCA , IEEE802154_TX_MODE_COMMON_COUNT , IEEE802154_TX_MODE_PRIV_START = IEEE802154_TX_MODE_COMMON_COUNT }
```

相关声明：[ieee802154_tx_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gab2bee8752291e082cb277145cef1225d)、[IEEE802154_TX_MODE_DIRECT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225da6904c3c7f53d46c5c8b41dd1a82b2650)、[IEEE802154_TX_MODE_CCA](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225da1e23f1ad3f9d0832fd4d67fc00fd8eb5)、[IEEE802154_TX_MODE_CSMA_CA](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225da51a0e7cb482447779634062655a1ec47)、[IEEE802154_TX_MODE_TXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225da9a7b8ba25603b72aecbf7f66abf26508)、[IEEE802154_TX_MODE_TXTIME_CCA](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225da42b4589afb2180fde053fdbbf58c0d3e)、[IEEE802154_TX_MODE_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225daa389aeccad62a0516678564e68fcd595)、[IEEE802154_TX_MODE_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225dabbab0c864f313ee4045e5ad59ea774e2)。

IEEE 802.15.4 发送模式（Transmission Mode）。

<a id="r_gab593bc6640ddea23c951982ca2f4c0bf"></a>

```c
enum ieee802154_fpb_mode { IEEE802154_FPB_ADDR_MATCH_THREAD , IEEE802154_FPB_ADDR_MATCH_ZIGBEE }
```

相关声明：[ieee802154_fpb_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gab593bc6640ddea23c951982ca2f4c0bf)、[IEEE802154_FPB_ADDR_MATCH_THREAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab593bc6640ddea23c951982ca2f4c0bfa012874ab4d234bbeb2954756cf2dc9d6)、[IEEE802154_FPB_ADDR_MATCH_ZIGBEE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab593bc6640ddea23c951982ca2f4c0bfac7c839b7c0649d6151f90ff1d51ae417)。

IEEE 802.15.4 帧待发位表地址匹配模式（Frame Pending Bit Table Address Matching Mode）。

<a id="r_ga34aecc5996174a812b295a3a4693ad09"></a>

```c
enum ieee802154_config_type { IEEE802154_CONFIG_AUTO_ACK_FPB , IEEE802154_CONFIG_ACK_FPB , IEEE802154_CONFIG_PAN_COORDINATOR , IEEE802154_CONFIG_PROMISCUOUS , IEEE802154_CONFIG_EVENT_HANDLER , IEEE802154_CONFIG_MAC_KEYS , IEEE802154_CONFIG_FRAME_COUNTER , IEEE802154_CONFIG_FRAME_COUNTER_IF_LARGER , IEEE802154_CONFIG_RX_SLOT , IEEE802154_CONFIG_CSL_PERIOD , IEEE802154_CONFIG_EXPECTED_RX_TIME , IEEE802154_CONFIG_ENH_ACK_HEADER_IE , IEEE802154_CONFIG_RX_ON_WHEN_IDLE , IEEE802154_CONFIG_CSMA_CA_BACKOFFS , IEEE802154_CONFIG_COMMON_COUNT , IEEE802154_CONFIG_PRIV_START = IEEE802154_CONFIG_COMMON_COUNT }
```

相关声明：[ieee802154_config_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga34aecc5996174a812b295a3a4693ad09)、[IEEE802154_CONFIG_AUTO_ACK_FPB](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a38c67aac70d24b31996871fe4686d9ee)、[IEEE802154_CONFIG_ACK_FPB](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09ab897aea56ea5e9ddf306c5c0d75c2cd7)、[IEEE802154_CONFIG_PAN_COORDINATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09ab2b6ae3034fb469168ed29704ec045f0)、[IEEE802154_CONFIG_PROMISCUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a399313ff2d8ebb3a2d72152a9615d8c5)、[IEEE802154_CONFIG_EVENT_HANDLER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a8d88a76f71cf8869b3e35e423b18c6f3)、[IEEE802154_CONFIG_MAC_KEYS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a8bd29c6d6aa67adaf23415eb337904c0)、[IEEE802154_CONFIG_FRAME_COUNTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09aad7d04b7e1c02b2d88fcbb8ab1ac313b)、[IEEE802154_CONFIG_FRAME_COUNTER_IF_LARGER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09aa34da77f0966ff5a0e8ac73ed68554a8)、[IEEE802154_CONFIG_RX_SLOT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6)、[IEEE802154_CONFIG_CSL_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a9fdbe95e0b7141d9150eaa4a5793c2e7)、[IEEE802154_CONFIG_EXPECTED_RX_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a1a71ef76d90b6882196e4c6473de6bd8)、[IEEE802154_CONFIG_ENH_ACK_HEADER_IE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a840e5f1db9a354e7bcd892ddb4117907)、[IEEE802154_CONFIG_RX_ON_WHEN_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a9228dbe2583e5be10f64b116e87645e1)、[IEEE802154_CONFIG_CSMA_CA_BACKOFFS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a2b8dbb8a7de613b8ca81513242958837)、[IEEE802154_CONFIG_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a61df14aeb348cfc694d539b506dc23ac)、[IEEE802154_CONFIG_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a1653b2869208045415d83fc6708d015c)。

IEEE 802.15.4 驱动配置类型（Driver Configuration Types）。

<a id="r_gaf4deddd3f23ebfd65fa47c5d62634430"></a>

```c
enum ieee802154_attr { IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_PAGES , IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_RANGES , IEEE802154_ATTR_PHY_HRP_UWB_SUPPORTED_PRFS , IEEE802154_ATTR_COMMON_COUNT , IEEE802154_ATTR_PRIV_START = IEEE802154_ATTR_COMMON_COUNT }
```

相关声明：[ieee802154_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf4deddd3f23ebfd65fa47c5d62634430)、[IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_PAGES](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430a4ad28f920776c45af9d430db786a926a)、[IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_RANGES](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430aba76daa0a70bcdd573ecbfd63ca19e7d)、[IEEE802154_ATTR_PHY_HRP_UWB_SUPPORTED_PRFS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430ad90b4a118866c4942ef6f6a8ae56eb3f)、[IEEE802154_ATTR_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430aa0830214987de7a89297777c0d1004de)、[IEEE802154_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430ad4912dc68abc1abe54bc212f023bf511)。

IEEE 802.15.4 驱动属性（Driver Attributes）。

<a id="r_ga8c9ab3cecefe641a25f003eb6d014fc5"></a>

```c
typedef void(* energy_scan_done_cb_t) (const struct device *dev, int16_t max_ed)
```

相关声明：[energy_scan_done_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga8c9ab3cecefe641a25f003eb6d014fc5)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

能量扫描回调（Energy Scan Callback）。

<a id="r_ga8219b80b8b179fc3a2ffac0dfdfb4e4b"></a>

```c
typedef void(* ieee802154_event_cb_t) (const struct device *dev, enum ieee802154_event evt, void *event_params)
```

相关声明：[ieee802154_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga8219b80b8b179fc3a2ffac0dfdfb4e4b)、[device](../device_reference/P002_设备对象结构.md)、[ieee802154_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga3491982b677941442d904ce69fce7c5e)。

驱动事件回调（Driver Event Callback）。

<a id="r_gaf69d2b65aa46ec4483c6bab419413ba5"></a>

```c
static int ieee802154_attr_get_channel_page_and_range (enum ieee802154_attr attr, const enum ieee802154_phy_channel_page phy_supported_channel_page, const struct ieee802154_phy_supported_channels *phy_supported_channels, struct ieee802154_attr_value *value)
```

相关声明：[ieee802154_attr_get_channel_page_and_range](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf69d2b65aa46ec4483c6bab419413ba5)、[ieee802154_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf4deddd3f23ebfd65fa47c5d62634430)、[ieee802154_phy_channel_page](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gacabc7386bea701373dfb36ab65bd36a9)、[ieee802154_phy_supported_channels](../network_core_model_reference/P040_ieee802154_phy_supported_channels_结构体.md)、[ieee802154_attr_value](../network_core_model_reference/P005_ieee802154_attr_value_结构体.md)。

处理信道页与范围（Channel Page and Range）的辅助函数，供驱动的 attr_get() 实现调用。


## 7.7\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [zephyr/net/net_pkt.h](../api_source_packet_gnss_reference/P006_net_pkt.h_源码浏览.md)
- [zephyr/net/net_time.h](../api_source_supplement_reference/P125_net_time.h_源码浏览.md)
- [zephyr/net/ieee802154.h](../api_source_configuration_reference/P031_ieee802154.h_源码浏览.md)
- [zephyr/net/ieee802154_ie.h](../api_source_network_reference/P009_ieee802154_ie.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_network_reference/P010_ieee802154_radio.h_源码浏览.md)
- [ieee802154_phy_channel_range](../network_core_model_reference/P039_ieee802154_phy_channel_range_结构体.md)
- [ieee802154_phy_supported_channels](../network_core_model_reference/P040_ieee802154_phy_supported_channels_结构体.md)
- [IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_RANGES](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430aba76daa0a70bcdd573ecbfd63ca19e7d)
- [ieee802154_filter](../network_core_model_reference/P017_ieee802154_filter_结构体.md)
- [ieee802154_radio_api::filter](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#aa9502e0e014a8d05ffe235567e8c98f3)
- [ieee802154_key](../network_core_model_reference/P032_ieee802154_key_结构体.md)
- [IEEE802154_CONFIG_MAC_KEYS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a8bd29c6d6aa67adaf23415eb337904c0)
- [ieee802154_config](../network_core_model_reference/P014_ieee802154_config_结构体.md)
- [ieee802154_attr_value](../network_core_model_reference/P005_ieee802154_attr_value_结构体.md)
- [ieee802154_radio_api](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md)
- [IEEE802154_PHY_SYMBOLS_PER_SECOND](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf228d9c26cedd5c790b7ebae41b5f937)
- [IEEE802154_MAC_A_BASE_SLOT_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gadb590005c9120e6b04aa430ebb306b8f)
- [IEEE802154_MAC_A_NUM_SUPERFRAME_SLOTS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga662c1add47deb9807e848aeeee5e6842)
- [IEEE802154_MAC_A_BASE_SUPERFRAME_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga52358c63c386b72f190d3b487c9ba286)
- [IEEE802154_MAC_A_UNIT_BACKOFF_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga86f3186304b02de3096d521238d407db)
- [IEEE802154_MAC_RESPONSE_WAIT_TIME_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga132be1037c5db1311c6d0c7d74e1fe40)
- [IEEE802154_PHY_A_TURNAROUND_TIME_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga9e95bf5d8ddb1087cdd9eb2aa80d100e)
- [IEEE802154_PHY_A_TURNAROUND_TIME_1MS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga68115b80097b116b704431808469450b)
- [IEEE802154_PHY_A_CCA_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf58b5d421167c2075dcdfdbaba5956dd)
- [IEEE802154_PHY_OQPSK_868MHZ_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga32ce931f3d35d779e4251c37f61583f5)
- [IEEE802154_PHY_OQPSK_780_TO_2450MHZ_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaff3d58945d53e824f1fb1ca11dd9997b)
- [IEEE802154_PHY_BPSK_868MHZ_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga1dc4319d0a8d979c7455e1f71f45d885)
- [IEEE802154_PHY_BPSK_915MHZ_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaa12344b6a118995b63c5bd4bc3180efd)
- [IEEE802154_PHY_SUN_FSK_863MHZ_915MHZ_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga155b5b5a06311c1bde3f36e06d02ed7d)
- [IEEE802154_PHY_SUN_FSK_PHR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gac088ee6d01014a12169e74111ea61993)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [ieee802154_is_ar_flag_set](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf5d7bdde2a9774f9d90604a6e203bb07)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [网络分组库（Network Packet Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html)
- [net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)
- [ieee802154_handle_ack](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga68e1f89571ccbefef61a5496577337fc)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [ieee802154_init](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gad2a4cb5df84ffe20b83fc54dc9bcfc91)
- [IEEE802154_DEFINE_PHY_SUPPORTED_CHANNELS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga78d4df389a7bd11c55e5c7b683897a9b)
- [ieee802154_phy_channel_page](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gacabc7386bea701373dfb36ab65bd36a9)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_ZERO_OQPSK_2450_BPSK_868_915](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a72b17a977aeb6792f7d2016117f4b2f9)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_ONE_DEPRECATED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a371a12ec5d762b03058fb2532fa04e45)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_TWO_OQPSK_868_915](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a5776e0160927b83f4e4e8d6479aaf804)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_THREE_CSS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a6f71c162be118b0c2edce139753c867e)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_FOUR_HRP_UWB](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a68b93381ddc1184ff0ed13456cf4b6a8)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_FIVE_OQPSK_780](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a6ea456573a6ff8aed348a9dc547b2db7)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_SIX_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9ac13dda08becd3d4799d45ef02f774cc1)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_SEVEN_MSK](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a1f33467ec7659ef411b08f7a23663311)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_EIGHT_LRP_UWB](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9aa0ab080c8cdac42dbf80622d075854dc)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_NINE_SUN_PREDEFINED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a996b529c9c277d6d653d0e0ffb8b2902)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_TEN_SUN_FSK_GENERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a02a17ea787e99528b2a6a8f5107f2544)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_ELEVEN_OQPSK_2380](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9aad0644244fb5b6cba5a295e246722e94)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_TWELVE_LECIM](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a6d4023088a3607c072acebd3940340c7)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_THIRTEEN_RCC](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a56dd4ae42595ef0edb109c729e333b08)
- [IEEE802154_PHY_HRP_UWB_PRF4_TPSYM_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gabeb8a359ce54618aa7df3ee8f6a434bb)
- [IEEE802154_PHY_HRP_UWB_PRF16_TPSYM_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga0123679fba7ca668aa158813f1bf2302)
- [IEEE802154_PHY_HRP_UWB_PRF64_TPSYM_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga59f8ba8a01171c56da6f7ae7f8983bf7)
- [IEEE802154_PHY_HRP_UWB_ERDEV_TPSYM_SYMBOL_PERIOD_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaa25ba5b644e58cfc7de5ba5aa526ea71)
- [IEEE802154_PHY_HRP_UWB_RDEV](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gacfd2faf2c3072f8851abd74fe5148ec5)
- [IEEE802154_PHY_HRP_UWB_ERDEV](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gae02b981a3908b05b4bc0b7a2844c27c7)
- [ieee802154_phy_hrp_uwb_nominal_prf](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga13610aeef06372bc47d84464537fdded)
- [IEEE802154_PHY_HRP_UWB_PRF_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddeda4369c745ed378d8273a1014322f3029a)
- [IEEE802154_PHY_HRP_UWB_NOMINAL_4_M](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddeda9dc3c58366502aeab04a208937536369)
- [IEEE802154_PHY_HRP_UWB_NOMINAL_16_M](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddedadf9230e6ef62ce66129bfe24f537c88a)
- [IEEE802154_PHY_HRP_UWB_NOMINAL_64_M](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddeda2b24236d3531cab7d21673d065b7c29e)
- [IEEE802154_PHY_HRP_UWB_NOMINAL_64_M_BPRF](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddedad920ae285cdcc2a4d59f7c23e29dce27)
- [IEEE802154_PHY_HRP_UWB_NOMINAL_128_M_HPRF](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddedae6c88efd301a449b1a31e8aedf4e30ca)
- [IEEE802154_PHY_HRP_UWB_NOMINAL_256_M_HPRF](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddedacb66442cf2a5e4c539b6b7edf8419be1)
- [IEEE802154_HW_CAPS_BITS_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf143a9f110a2eb6b21104af6927159bc)
- [ieee802154_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf99cda89c29df3c0088fc57ec09cbcd4)
- [IEEE802154_HW_CAPS_BITS_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga40912ccb268768b4e96ce9cad35476af)
- [IEEE802154_CONFIG_RX_SLOT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga1cb6434a3a7555fe9d35c73b698cbf10)
- [IEEE802154_CONFIG_RX_SLOT_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga3828a2d56a39de92c2fd79caaac4c800)
- [IEEE802154_HW_ENERGY_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a179ad073a5bd34e4e4af587d07ca3f73)
- [IEEE802154_HW_FCS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a0ea21cab335dd9082feb2d08be0eb5fa)
- [IEEE802154_HW_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4afd09f329a708d00f1384a50c59ddde27)
- [IEEE802154_HW_PROMISC](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a4adb33f2ca81a24244dead6b379cd916)
- [IEEE802154_HW_CSMA](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a2ee53f11e1ed6853e1f5d9dfe7d7bdf7)
- [IEEE802154_HW_TX_RX_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4ab383a932c0ac9deece68f02210089119)
- [IEEE802154_HW_RETRANSMISSION](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a752472a994bdcbdf9cdf86deb0231849)
- [IEEE802154_HW_RX_TX_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4aec16c4d418117de2d106e84297568b03)
- [IEEE802154_HW_TXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a435d032f42d509bd78a992de6e4d7b1d)
- [IEEE802154_HW_RXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a68ae68c83a87f0efc25f74edd80c4600)
- [IEEE802154_HW_TX_SEC](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a7924c3d5bfe6dceeb2e8caa6df7edecb)
- [IEEE802154_RX_ON_WHEN_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4ac1e00966043e5884c4cbd65fb26f0c0b)
- [IEEE802154_HW_SELECTIVE_TXCHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4ab6cf4f3552d6193027a538a13b95952e)
- [ieee802154_filter_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaa1971591e72866d0f3f0d4db2931e25a)
- [IEEE802154_FILTER_TYPE_IEEE_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaa1971591e72866d0f3f0d4db2931e25aa928a93b536c6408b3d77aa329c274fe8)
- [IEEE802154_FILTER_TYPE_SHORT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaa1971591e72866d0f3f0d4db2931e25aa2fa1ac98a3b870fcf6e85e7ec82cfbe9)
- [IEEE802154_FILTER_TYPE_PAN_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaa1971591e72866d0f3f0d4db2931e25aab44cc830999926a5d232aedabef52653)
- [IEEE802154_FILTER_TYPE_SRC_IEEE_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaa1971591e72866d0f3f0d4db2931e25aade18e03611339f5f7ec4fdcdee409c21)
- [IEEE802154_FILTER_TYPE_SRC_SHORT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaa1971591e72866d0f3f0d4db2931e25aac6dbb68674e7594fd4cd69bbe4ea60de)
- [ieee802154_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga3491982b677941442d904ce69fce7c5e)
- [IEEE802154_EVENT_TX_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga3491982b677941442d904ce69fce7c5eaacd61f4466f1ef926adc9e1afe6c1648)
- [IEEE802154_EVENT_RX_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga3491982b677941442d904ce69fce7c5eaef51197ca09befaee8cdfa2cde107273)
- [IEEE802154_EVENT_RX_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga3491982b677941442d904ce69fce7c5eaf7ed46b9d13a232a2ea6b650514eea3d)
- [IEEE802154_CONFIG_EVENT_HANDLER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a8d88a76f71cf8869b3e35e423b18c6f3)
- [ieee802154_rx_fail_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga04febbd15f9e6f6540d711ada5a4a1c8)
- [IEEE802154_RX_FAIL_NOT_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8ad584824b4813626d04a85499371b9c32)
- [IEEE802154_RX_FAIL_INVALID_FCS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8a103f6683ff71f4f7248ee1a0d09d6be4)
- [IEEE802154_RX_FAIL_ADDR_FILTERED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8a7ff9cfcc5e4dfc2bf7abe1860a39410f)
- [IEEE802154_RX_FAIL_NO_BUFS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8a7e180466cd23edf5f030c3fbefadf2d1)
- [IEEE802154_RX_FAIL_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8a7bd7daaf3823d86ed48782138b671e57)
- [IEEE802154_RX_FAIL_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8a5baa9dd683a717f7fbdfc5ab85935a3b)
- [ieee802154_tx_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gab2bee8752291e082cb277145cef1225d)
- [IEEE802154_TX_MODE_DIRECT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225da6904c3c7f53d46c5c8b41dd1a82b2650)
- [IEEE802154_TX_MODE_CCA](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225da1e23f1ad3f9d0832fd4d67fc00fd8eb5)
- [IEEE802154_TX_MODE_CSMA_CA](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225da51a0e7cb482447779634062655a1ec47)
- [IEEE802154_TX_MODE_TXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225da9a7b8ba25603b72aecbf7f66abf26508)
- [IEEE802154_TX_MODE_TXTIME_CCA](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225da42b4589afb2180fde053fdbbf58c0d3e)
- [IEEE802154_TX_MODE_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225daa389aeccad62a0516678564e68fcd595)
- [IEEE802154_TX_MODE_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225dabbab0c864f313ee4045e5ad59ea774e2)
- [ieee802154_fpb_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gab593bc6640ddea23c951982ca2f4c0bf)
- [IEEE802154_FPB_ADDR_MATCH_THREAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab593bc6640ddea23c951982ca2f4c0bfa012874ab4d234bbeb2954756cf2dc9d6)
- [IEEE802154_FPB_ADDR_MATCH_ZIGBEE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab593bc6640ddea23c951982ca2f4c0bfac7c839b7c0649d6151f90ff1d51ae417)
- [ieee802154_config_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga34aecc5996174a812b295a3a4693ad09)
- [IEEE802154_CONFIG_AUTO_ACK_FPB](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a38c67aac70d24b31996871fe4686d9ee)
- [IEEE802154_CONFIG_ACK_FPB](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09ab897aea56ea5e9ddf306c5c0d75c2cd7)
- [IEEE802154_CONFIG_PAN_COORDINATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09ab2b6ae3034fb469168ed29704ec045f0)
- [IEEE802154_CONFIG_PROMISCUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a399313ff2d8ebb3a2d72152a9615d8c5)
- [IEEE802154_CONFIG_FRAME_COUNTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09aad7d04b7e1c02b2d88fcbb8ab1ac313b)
- [IEEE802154_CONFIG_FRAME_COUNTER_IF_LARGER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09aa34da77f0966ff5a0e8ac73ed68554a8)
- [IEEE802154_CONFIG_RX_SLOT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6)
- [IEEE802154_CONFIG_CSL_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a9fdbe95e0b7141d9150eaa4a5793c2e7)
- [IEEE802154_CONFIG_EXPECTED_RX_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a1a71ef76d90b6882196e4c6473de6bd8)
- [IEEE802154_CONFIG_ENH_ACK_HEADER_IE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a840e5f1db9a354e7bcd892ddb4117907)
- [IEEE802154_CONFIG_RX_ON_WHEN_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a9228dbe2583e5be10f64b116e87645e1)
- [IEEE802154_CONFIG_CSMA_CA_BACKOFFS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a2b8dbb8a7de613b8ca81513242958837)
- [IEEE802154_CONFIG_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a61df14aeb348cfc694d539b506dc23ac)
- [IEEE802154_CONFIG_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a1653b2869208045415d83fc6708d015c)
- [ieee802154_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf4deddd3f23ebfd65fa47c5d62634430)
- [IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_PAGES](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430a4ad28f920776c45af9d430db786a926a)
- [IEEE802154_ATTR_PHY_HRP_UWB_SUPPORTED_PRFS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430ad90b4a118866c4942ef6f6a8ae56eb3f)
- [IEEE802154_ATTR_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430aa0830214987de7a89297777c0d1004de)
- [IEEE802154_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430ad4912dc68abc1abe54bc212f023bf511)
- [energy_scan_done_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga8c9ab3cecefe641a25f003eb6d014fc5)
- [device](../device_reference/P002_设备对象结构.md)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [ieee802154_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga8219b80b8b179fc3a2ffac0dfdfb4e4b)
- [ieee802154_attr_get_channel_page_and_range](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf69d2b65aa46ec4483c6bab419413ba5)

<a id="header-details"></a>

---

[上一章](P006_zephyr__dt-bindings__clock__em32_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__drivers__interrupt_controller__intc_mchp_eic_g1.h_文件参考.md)
