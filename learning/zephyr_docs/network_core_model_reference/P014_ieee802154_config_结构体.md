---
id: learning.zephyr-docs.network-core-model-reference.page-14
title: ieee802154_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_ieee802154\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IEEE 802.15.4驱动的配置数据（Configuration Data）。

```c
#include <zephyr/net/ieee802154_radio.h>
```

<a id="details"></a>

IEEE 802.15.4驱动的配置数据（Configuration Data）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

```c
union {
```

```c
struct {
```

<a id="r_a539248fe44055988b68d80c65cb0c81e"></a>

```c
bool enabled
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enabled](#ad9361f9ba1652e46d0be25e0de39afdf)。

是否启用自动确认帧待处理位（Auto ACK FPB）。

<a id="r_a2d4acc8c9b479dcf36fc8286081fabbb"></a>

```c
enum ieee802154_fpb_mode mode
```

相关声明：[ieee802154_fpb_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gab593bc6640ddea23c951982ca2f4c0bf)、[mode](#ad139acde94327d4b8ceb76760751521d)。

自动确认帧待处理位模式（Auto ACK FPB Mode）。

<a id="r_a11d36000631cf4b9489b8aa84a544754"></a>

```c
} auto_ack_fpb
```

相关声明：[auto_ack_fpb](#ab27a654a0d53f268199e95dc21e18fd4)。

参见（See）：`IEEE802154_CONFIG_AUTO_ACK_FPB`。

```c
struct {
```

<a id="r_a64bd4b31cc2be60ff37770479d76a27e"></a>

```c
uint8_t * addr
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[addr](#a673f5cceb6439bc1c3527c62062151d1)。

短地址和扩展地址均采用小端序（Little Endian）。

<a id="r_a6f1959014f4870ac47fcee5173bf6908"></a>

```c
bool extended
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[extended](#a55823097d62a69d0c92dc70fb4ff1dd5)。

是否为扩展地址（Extended Address）。

<a id="r_af4fe07c9d3bc7d2e3c3477238d299e5c"></a>

```c
bool enabled
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enabled](#ad9361f9ba1652e46d0be25e0de39afdf)。

是否启用（Enabled）。

<a id="r_a210cdb99dbd18fc4c0bc2c6c4fc733d7"></a>

```c
} ack_fpb
```

相关声明：[ack_fpb](#a3a5e597e53bfcc9e3bed8bac2edb74d2)。

参见（See）：`IEEE802154_CONFIG_ACK_FPB`。

<a id="r_a18f44280c11b5f9105ad86e3f4001cf0"></a>

```c
bool pan_coordinator
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[pan_coordinator](#a078ec577af3d170781ed770c80c54b72)。

参见（See）：`IEEE802154_CONFIG_PAN_COORDINATOR`。

<a id="r_ae6ed15aa5e2108ff15b367d533281e68"></a>

```c
bool promiscuous
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[promiscuous](#aafb11c4130ff39e5c40dfe5d32c0d4e7)。

参见（See）：`IEEE802154_CONFIG_PROMISCUOUS`。

<a id="r_a38635a7d1aa3028b6b7f9e55c749bfe6"></a>

```c
bool rx_on_when_idle
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[rx_on_when_idle](#a8b7d4804cd051d69f3602f35cb4a8630)。

参见（See）：`IEEE802154_CONFIG_RX_ON_WHEN_IDLE`。

<a id="r_ab32b07abb252ea52cfaa4f36f5dbf79a"></a>

```c
ieee802154_event_cb_t event_handler
```

相关声明：[ieee802154_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga8219b80b8b179fc3a2ffac0dfdfb4e4b)、[event_handler](#a1558e71a1d5ab74990964ff4deabbdb7)。

参见（See）：`IEEE802154_CONFIG_EVENT_HANDLER`。

<a id="r_a82c6ed6801d678d1c92d80a66b4c1db9"></a>

```c
uint8_t csma_ca_backoffs
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[csma_ca_backoffs](#afa1d230e1059013a7a99e737da3a0266)。

参见（See）：`IEEE802154_CONFIG_CSMA_CA_BACKOFFS`。

<a id="r_a46a26b9cb789446fcbfa0082f7174cb5"></a>

```c
struct ieee802154_key * mac_keys
```

相关声明：[ieee802154_key](P032_ieee802154_key_结构体.md)、[mac_keys](#a942c0d4fb244c7256530536dc132a727)。

参见（See）：`IEEE802154_CONFIG_MAC_KEYS`。

<a id="r_adde95d605c7df37954878a5d94900a70"></a>

```c
uint32_t frame_counter
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[frame_counter](#a272cfd864c7d47c6f06f26871ce07fb6)。

参见（See）：`IEEE802154_CONFIG_FRAME_COUNTER`。

```c
struct {
```

<a id="r_ad109b4802af2ae95821885625f83fe9a"></a>

```c
net_time_t start
```

相关声明：[net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)、[start](#a86b72101b0b21622f3cc8a2b3877e356)。

相对于网络子系统本地时钟的纳秒分辨率时间戳（Timestamp），定义预期接收器正在监听的接收窗口（RX Window）的开始时刻（即：

<a id="r_aefff316a2cb73194cad545c8cb7a3e28"></a>

```c
net_time_t duration
```

相关声明：[net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)、[duration](#ab36833b4311b03f08f67290f4edd8e41)。

相对于上述接收窗口起点、以纳秒分辨率表示的接收窗口持续时间（Duration），窗口内预期接收器正在监听（即：

<a id="r_a504184baf0968ac3801f74bbebba3199"></a>

```c
uint8_t channel
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel](#a8f7efaa743e070479632d139f0fc57c0)。

使用的信道（Channel）。

<a id="r_ae9d9db59a99c2d549456973e121136d2"></a>

```c
} rx_slot
```

相关声明：[rx_slot](#aadc2714bf31484cce071e9ef7b9a4007)。

参见（See）：`IEEE802154_CONFIG_RX_SLOT`。

<a id="r_af8d6ff87bc1ca9a552fbd058fb9802ca"></a>

```c
uint32_t csl_period
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[csl_period](#a5106a759148ec20c6c6c83a2581c9e88)。

参见（See）：`IEEE802154_CONFIG_CSL_PERIOD`。

<a id="r_a8b4014a8066e44a24529462cf90bbeb6"></a>

```c
net_time_t expected_rx_time
```

相关声明：[net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)、[expected_rx_time](#a8124aed4a4af36c0e21fd8f1b1c97e3e)。

参见（See）：`IEEE802154_CONFIG_EXPECTED_RX_TIME`。

```c
struct {
```

<a id="r_a73bb20eb21c0324f62132aa9c14d4e93"></a>

```c
struct ieee802154_header_ie * header_ie
```

相关声明：[header_ie](#a5343dec0de835943c0bef2c2d603a91d)。

指向头部信息元素（Header IE）的指针，见第7.4.2.1节图7-21。

<a id="r_a4c3832b5eadf98780ce7b4efab227010"></a>

```c
const uint8_t * ext_addr
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ext_addr](#a03d6ec1a371312961f3a1ee42e113bbf)。

按扩展地址（Extended Address）筛选将接收此信息元素（IE）的设备。

<a id="r_a8d2d567258f60be842f414bca8c60637"></a>

```c
uint16_t short_addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[short_addr](#aa27066dd9e54dab6795332b7413670f5)。

按短地址（Short Address）筛选将接收此信息元素（IE）的设备。

<a id="r_acef8e7d7d34ed75efa10de4f0255629f"></a>

```c
bool purge_ie
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[purge_ie](#a8971a91be8748bd45027fcb730b99639)。

清除增强确认头部信息元素（Enhanced ACK Header IEs）的标志。

<a id="r_a40724f7b57af94dd0ce2436c016bd4ed"></a>

```c
} ack_ie
```

相关声明：[ack_ie](#a39c06e32cb4a74b4d8a9864f714e8c93)。

参见（See）：`IEEE802154_CONFIG_ENH_ACK_HEADER_IE`。

<a id="r_a4e62cce9f7735b5bb3a53b95d886b13d"></a>

```c
};
```

配置数据（Configuration Data）。

## 14.2\_详细说明（Detailed Documentation）

<a id="a4e62cce9f7735b5bb3a53b95d886b13d"></a>

### `[union]`

```c
union { ... } ieee802154_config
```

配置数据（Configuration Data）。

<a id="a3a5e597e53bfcc9e3bed8bac2edb74d2"></a>

### `[struct]`

```c
struct { ... } ieee802154_config::ack_fpb
```

参见（See）：`IEEE802154_CONFIG_ACK_FPB`。

<a id="a39c06e32cb4a74b4d8a9864f714e8c93"></a>

### `[struct]`

```c
struct { ... } ieee802154_config::ack_ie
```

参见（See）：`IEEE802154_CONFIG_ENH_ACK_HEADER_IE`。

<a id="a673f5cceb6439bc1c3527c62062151d1"></a>

### `addr`

```c
uint8_t* ieee802154_config::addr
```

短地址和扩展地址均采用小端序（Little Endian）。

<a id="ab27a654a0d53f268199e95dc21e18fd4"></a>

### `[struct]`

```c
struct { ... } ieee802154_config::auto_ack_fpb
```

参见（See）：`IEEE802154_CONFIG_AUTO_ACK_FPB`。

<a id="a8f7efaa743e070479632d139f0fc57c0"></a>

### `channel`

```c
uint8_t ieee802154_config::channel
```

使用的信道（Channel）。

<a id="a5106a759148ec20c6c6c83a2581c9e88"></a>

### `csl_period`

```c
uint32_t ieee802154_config::csl_period
```

参见（See）：`IEEE802154_CONFIG_CSL_PERIOD`。

采用CPU字节序（CPU Byte Order）。

<a id="afa1d230e1059013a7a99e737da3a0266"></a>

### `csma_ca_backoffs`

```c
uint8_t ieee802154_config::csma_ca_backoffs
```

参见（See）：`IEEE802154_CONFIG_CSMA_CA_BACKOFFS`。

<a id="ab36833b4311b03f08f67290f4edd8e41"></a>

### `duration`

```c
net_time_t ieee802154_config::duration
```

相对于上述接收窗口起点、以纳秒分辨率表示的接收窗口持续时间（Duration），窗口内预期接收器正在监听（即：

不包含任何关闭时间）。仅允许大于等于0的值。

将持续时间（Duration）设为0会禁用接收器，与start参数无关。

<a id="ad9361f9ba1652e46d0be25e0de39afdf"></a>

### `enabled`

```c
bool ieee802154_config::enabled
```

是否启用自动确认帧待处理位（Auto ACK FPB）。

是否启用（Enabled）。

<a id="a1558e71a1d5ab74990964ff4deabbdb7"></a>

### `event_handler`

```c
ieee802154_event_cb_t ieee802154_config::event_handler
```

参见（See）：`IEEE802154_CONFIG_EVENT_HANDLER`。

<a id="a8124aed4a4af36c0e21fd8f1b1c97e3e"></a>

### `expected_rx_time`

```c
net_time_t ieee802154_config::expected_rx_time
```

参见（See）：`IEEE802154_CONFIG_EXPECTED_RX_TIME`。

<a id="a03d6ec1a371312961f3a1ee42e113bbf"></a>

### `ext_addr`

```c
const uint8_t* ieee802154_config::ext_addr
```

按扩展地址（Extended Address）筛选将接收此信息元素（IE）的设备。

可以（MAY）设为NULL，以为全部设备配置回退值；这意味着short_addr也必须（MUST）设为IEEE802154_BROADCAST_ADDRESS。

采用大端序（Big Endian）。

<a id="a55823097d62a69d0c92dc70fb4ff1dd5"></a>

### `extended`

```c
bool ieee802154_config::extended
```

是否为扩展地址（Extended Address）。

<a id="a272cfd864c7d47c6f06f26871ce07fb6"></a>

### `frame_counter`

```c
uint32_t ieee802154_config::frame_counter
```

参见（See）：`IEEE802154_CONFIG_FRAME_COUNTER`。

<a id="a5343dec0de835943c0bef2c2d603a91d"></a>

### `header_ie`

```c
struct ieee802154_header_ie* ieee802154_config::header_ie
```

指向头部信息元素（Header IE）的指针，见第7.4.2.1节图7-21。

某些头部信息元素（Header IEs）需要在运行时即时注入时序信息，因此可能不完整；见IEEE802154_CONFIG_ENH_ACK_HEADER_IE中的列表。

<a id="a942c0d4fb244c7256530536dc132a727"></a>

### `mac_keys`

```c
struct ieee802154_key* ieee802154_config::mac_keys
```

参见（See）：`IEEE802154_CONFIG_MAC_KEYS`。

指向密钥数组的指针，数组列出用于MAC加密（MAC Encryption）的密钥。参见IEEE 802.15.4中的secKeyIdLookupDescriptor和secKeyDescriptor。

key_value字段指向包含16字节密钥的缓冲区。驱动应当（SHALL）在调用返回之前复制该缓冲区。

此变长数组（Variable Length Array）以key_value字段设为NULL的条目终止。

<a id="ad139acde94327d4b8ceb76760751521d"></a>

### `mode`

```c
enum ieee802154_fpb_mode ieee802154_config::mode
```

自动确认帧待处理位模式（Auto ACK FPB Mode）。

<a id="a078ec577af3d170781ed770c80c54b72"></a>

### `pan_coordinator`

```c
bool ieee802154_config::pan_coordinator
```

参见（See）：`IEEE802154_CONFIG_PAN_COORDINATOR`。

<a id="aafb11c4130ff39e5c40dfe5d32c0d4e7"></a>

### `promiscuous`

```c
bool ieee802154_config::promiscuous
```

参见（See）：`IEEE802154_CONFIG_PROMISCUOUS`。

<a id="a8971a91be8748bd45027fcb730b99639"></a>

### `purge_ie`

```c
bool ieee802154_config::purge_ie
```

清除增强确认头部信息元素（Enhanced ACK Header IEs）的标志。

标志设为true时，驱动应移除全部现有头部信息元素（Header IEs），并忽略config中的所有其他条目。这意味着不允许在同一次调用中既清除当前头部IE，又配置新的头部IE。

<a id="a8b7d4804cd051d69f3602f35cb4a8630"></a>

### `rx_on_when_idle`

```c
bool ieee802154_config::rx_on_when_idle
```

参见（See）：`IEEE802154_CONFIG_RX_ON_WHEN_IDLE`。

<a id="aadc2714bf31484cce071e9ef7b9a4007"></a>

### `[struct]`

```c
struct { ... } ieee802154_config::rx_slot
```

参见（See）：`IEEE802154_CONFIG_RX_SLOT`。

<a id="aa27066dd9e54dab6795332b7413670f5"></a>

### `short_addr`

```c
uint16_t ieee802154_config::short_addr
```

按短地址（Short Address）筛选将接收此信息元素（IE）的设备。

可以（MAY）设为IEEE802154_BROADCAST_ADDRESS，以为全部设备配置回退值；这意味着此时ext_addr也必须（MUST）设为NULL。

采用CPU字节序（CPU Byte Order）。

<a id="a86b72101b0b21622f3cc8a2b3877e356"></a>

### `start`

```c
net_time_t ieee802154_config::start
```

相对于网络子系统本地时钟的纳秒分辨率时间戳（Timestamp），定义预期接收器正在监听的接收窗口（RX Window）的开始时刻（即：

不包含任何驱动启动时间）。

把rx_slot的start属性设为-1，会取消并删除先前活动的接收时隙（RX Slot）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_radio.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_radio.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [ieee802154_fpb_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gab593bc6640ddea23c951982ca2f4c0bf)
- [IEEE802154_CONFIG_AUTO_ACK_FPB](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a38c67aac70d24b31996871fe4686d9ee)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [IEEE802154_CONFIG_ACK_FPB](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09ab897aea56ea5e9ddf306c5c0d75c2cd7)
- [IEEE802154_CONFIG_PAN_COORDINATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09ab2b6ae3034fb469168ed29704ec045f0)
- [IEEE802154_CONFIG_PROMISCUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a399313ff2d8ebb3a2d72152a9615d8c5)
- [IEEE802154_CONFIG_RX_ON_WHEN_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a9228dbe2583e5be10f64b116e87645e1)
- [ieee802154_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga8219b80b8b179fc3a2ffac0dfdfb4e4b)
- [IEEE802154_CONFIG_EVENT_HANDLER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a8d88a76f71cf8869b3e35e423b18c6f3)
- [IEEE802154_CONFIG_CSMA_CA_BACKOFFS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a2b8dbb8a7de613b8ca81513242958837)
- [ieee802154_key](P032_ieee802154_key_结构体.md)
- [IEEE802154_CONFIG_MAC_KEYS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a8bd29c6d6aa67adaf23415eb337904c0)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [IEEE802154_CONFIG_FRAME_COUNTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09aad7d04b7e1c02b2d88fcbb8ab1ac313b)
- [net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)
- [IEEE802154_CONFIG_RX_SLOT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6)
- [IEEE802154_CONFIG_CSL_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a9fdbe95e0b7141d9150eaa4a5793c2e7)
- [IEEE802154_CONFIG_EXPECTED_RX_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a1a71ef76d90b6882196e4c6473de6bd8)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [IEEE802154_CONFIG_ENH_ACK_HEADER_IE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a840e5f1db9a354e7bcd892ddb4117907)
- [ieee802154_config](P014_ieee802154_config_结构体.md)
- [IEEE802154_BROADCAST_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gafae1906dc9b39c93690b127efaaacacb)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_ieee802154_command_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_ieee802154_context_结构体.md)
