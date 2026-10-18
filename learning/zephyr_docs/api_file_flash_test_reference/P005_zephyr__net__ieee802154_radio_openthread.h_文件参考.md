---
id: learning.zephyr-docs.api-file-flash-test-reference.page-5
title: zephyr__net__ieee802154_radio_openthread.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_net\_\_ieee802154\_radio\_openthread.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

此文件为OpenThread扩展ieee802154_radio.h的接口。

<a id="details"></a>

```c
#include <zephyr/net/ieee802154_radio.h>
```

查看此文件的源码。

此文件为OpenThread扩展ieee802154_radio.h的接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_ieee802154_5Fopenthread_5Fconfig"></a>

```c
struct ieee802154_openthread_config
```

相关声明：[ieee802154_openthread_config](../network_core_model_reference/P037_ieee802154_openthread_config_结构体.md)。

ieee802154驱动中OpenThread专用的配置数据。

<a id="r_ieee802154_5Fopenthread_5Fattr_5Fvalue"></a>

```c
struct ieee802154_openthread_attr_value
```

相关声明：[ieee802154_openthread_attr_value](../network_core_model_reference/P036_ieee802154_openthread_attr_value_结构体.md)。

ieee802154驱动中OpenThread专用的属性值数据。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_a83674b259d4cf5c28827385b27a499e2"></a>

```c
#define IEEE802154_OPENTHREAD_HW_CAPS_BITS_START IEEE802154_HW_CAPS_BITS_PRIV_START
```

相关声明：[IEEE802154_OPENTHREAD_HW_CAPS_BITS_START](#a83674b259d4cf5c28827385b27a499e2)、[IEEE802154_HW_CAPS_BITS_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga40912ccb268768b4e96ce9cad35476af)。

ieee802154 驱动中 OpenThread 专用能力（Capabilities）的起始位编号。

<a id="r_a3df2b5a9df519084df0ecdcb42a81d45"></a>

```c
#define IEEE802154_OPENTHREAD_THREAD_IE_VENDOR_OUI { 0x9b, 0xb8, 0xea }
```

相关声明：[IEEE802154_OPENTHREAD_THREAD_IE_VENDOR_OUI](#a3df2b5a9df519084df0ecdcb42a81d45)。

用于厂商专用头部或嵌套信息元素（Nested Information Elements）的 Thread 厂商组织唯一标识符（OUI）；参见 IEEE 802.15.4-2020 第 7.4.2.2 节和第 7.4.4.30 节。

<a id="r_a449d47ac13847e40a978a6fd80d5faed"></a>

```c
#define IEEE802154_OPENTHREAD_VENDOR_OUI_LEN 3
```

相关声明：[IEEE802154_OPENTHREAD_VENDOR_OUI_LEN](#a449d47ac13847e40a978a6fd80d5faed)。

IEEE 802.15.4-2020 厂商组织唯一标识符（Vendor OUI）的长度。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.3\_枚举（Enumerations）

<a id="r_a80bc0d04ae7e2286abe372df49880ac8"></a>

```c
enum ieee802154_openthread_hw_caps { IEEE802154_OPENTHREAD_HW_MULTIPLE_CCA = BIT( (13) ) , IEEE802154_OPENTHREAD_HW_CST = BIT( (13) + 1) }
```

相关声明：[ieee802154_openthread_hw_caps](#a80bc0d04ae7e2286abe372df49880ac8)、[IEEE802154_OPENTHREAD_HW_MULTIPLE_CCA](#a80bc0d04ae7e2286abe372df49880ac8a9a1663d68026c5156a0f127ae086adc8)、[IEEE802154_OPENTHREAD_HW_CST](#a80bc0d04ae7e2286abe372df49880ac8a8cd0cafed5d27222aff18e42b1693c7f)。

ieee802154 驱动的 OpenThread 专用能力（Capabilities）。

<a id="r_a038a7e158a73533b1fd55bb92e5fa64a"></a>

```c
enum ieee802154_openthread_tx_mode { IEEE802154_OPENTHREAD_TX_MODE_TXTIME_MULTIPLE_CCA = IEEE802154_TX_MODE_PRIV_START }
```

相关声明：[ieee802154_openthread_tx_mode](#a038a7e158a73533b1fd55bb92e5fa64a)、[IEEE802154_OPENTHREAD_TX_MODE_TXTIME_MULTIPLE_CCA](#a038a7e158a73533b1fd55bb92e5fa64aa75f9fb57cf10207c5142a86552cb401f)。

发送模式（TX Mode）。

<a id="r_ab11e7d5ec46577a0259d68349ac19525"></a>

```c
enum ieee802154_openthread_config_type { IEEE802154_OPENTHREAD_CONFIG_MAX_EXTRA_CCA_ATTEMPTS = IEEE802154_CONFIG_PRIV_START , IEEE802154_OPENTHREAD_CONFIG_CST_PERIOD , IEEE802154_OPENTHREAD_CONFIG_EXPECTED_TX_TIME }
```

相关声明：[ieee802154_openthread_config_type](#ab11e7d5ec46577a0259d68349ac19525)、[IEEE802154_OPENTHREAD_CONFIG_MAX_EXTRA_CCA_ATTEMPTS](#ab11e7d5ec46577a0259d68349ac19525ac06ead66659fa9a736d368a9d255bc95)、[IEEE802154_OPENTHREAD_CONFIG_CST_PERIOD](#ab11e7d5ec46577a0259d68349ac19525a2b1436aa0d7fdded8fda38b4ee8f2af7)、[IEEE802154_OPENTHREAD_CONFIG_EXPECTED_TX_TIME](#ab11e7d5ec46577a0259d68349ac19525a7ee21cd052527506e860b4a3bc772a04)。

ieee802154 驱动的 OpenThread 专用配置类型（Configuration Types）。

<a id="r_a15a4b5a53be4b2c867eb9551de7d914a"></a>

```c
enum ieee802154_openthread_attr { IEEE802154_OPENTHREAD_ATTR_T_RECCA = IEEE802154_ATTR_PRIV_START , IEEE802154_OPENTHREAD_ATTR_T_CCATX }
```

相关声明：[ieee802154_openthread_attr](#a15a4b5a53be4b2c867eb9551de7d914a)、[IEEE802154_OPENTHREAD_ATTR_T_RECCA](#a15a4b5a53be4b2c867eb9551de7d914aa4d92697c08b14201465db37b302c2fa5)、[IEEE802154_OPENTHREAD_ATTR_T_CCATX](#a15a4b5a53be4b2c867eb9551de7d914aa0e68340300b0e2d29811289fa7c1987b)。

ieee802154 驱动的 OpenThread 专用属性（Attributes）。

## 5.4\_详细说明（Detailed Documentation）

<a id="a83674b259d4cf5c28827385b27a499e2"></a>

### `IEEE802154_OPENTHREAD_HW_CAPS_BITS_START`

```c
#define IEEE802154_OPENTHREAD_HW_CAPS_BITS_START IEEE802154_HW_CAPS_BITS_PRIV_START
```

ieee802154 驱动中 OpenThread 专用能力（Capabilities）的起始位编号。

<a id="a3df2b5a9df519084df0ecdcb42a81d45"></a>

### `IEEE802154_OPENTHREAD_THREAD_IE_VENDOR_OUI`

```c
#define IEEE802154_OPENTHREAD_THREAD_IE_VENDOR_OUI { 0x9b, 0xb8, 0xea }
```

用于厂商专用头部或嵌套信息元素（Nested Information Elements）的 Thread 厂商组织唯一标识符（OUI）；参见 IEEE 802.15.4-2020 第 7.4.2.2 节和第 7.4.4.30 节。

采用小端序（Little Endian）。

<a id="a449d47ac13847e40a978a6fd80d5faed"></a>

### `IEEE802154_OPENTHREAD_VENDOR_OUI_LEN`

```c
#define IEEE802154_OPENTHREAD_VENDOR_OUI_LEN 3
```

IEEE 802.15.4-2020 厂商组织唯一标识符（Vendor OUI）的长度。

<a id="a15a4b5a53be4b2c867eb9551de7d914a"></a>

### `ieee802154_openthread_attr`

```c
enum ieee802154_openthread_attr
```

ieee802154 驱动的 OpenThread 专用属性（Attributes）。

此类型扩展 ieee802154_attr。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `IEEE802154_OPENTHREAD_ATTR_T_RECCA` | 属性：背靠背执行的连续空闲信道评估（CCA）之间的最大时间。 这是 IEEE802154_OPENTHREAD_TX_MODE_TXTIME_MULTIPLE_CCA 中所述 T_recca 参数对应的属性。时间单位为微秒。 |
| `IEEE802154_OPENTHREAD_ATTR_T_CCATX` | 属性：CCA 检测到信道空闲至本地天线开始发送同步头（SHR）之间的最大时间。 这是 IEEE802154_OPENTHREAD_TX_MODE_TXTIME_MULTIPLE_CCA 中所述 T_ccatx 参数对应的属性。时间单位为微秒。 |

<a id="ab11e7d5ec46577a0259d68349ac19525"></a>

### `ieee802154_openthread_config_type`

```c
enum ieee802154_openthread_config_type
```

ieee802154 驱动的 OpenThread 专用配置类型（Configuration Types）。

此类型扩展 ieee802154_config_type。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `IEEE802154_OPENTHREAD_CONFIG_MAX_EXTRA_CCA_ATTEMPTS` | 允许为采用 IEEE802154_OPENTHREAD_TX_MODE_TXTIME_MULTIPLE_CCA 模式请求的发送配置额外的空闲信道评估（CCA）。 需要 IEEE802154_OPENTHREAD_HW_MULTIPLE_CCA 能力（Capability）。 |
| `IEEE802154_OPENTHREAD_CONFIG_CST_PERIOD` | 配置设备的 CST 周期（CST Period）。 驱动即将发送包含 CST Period 信息元素（IE）的帧时，必须（SHALL）依据此配置参数值，将 CST Period 值填入该信息元素。 需要 IEEE802154_OPENTHREAD_HW_CST 能力（Capability）。 |
| `IEEE802154_OPENTHREAD_CONFIG_EXPECTED_TX_TIME` | 配置预计发送 TX 帧的时间点（Timepoint）。 驱动即将发送包含 CST Phase 信息元素（IE）的帧时，必须（SHALL）依据此配置参数值、发送时间和 CST Period 值，将 CST Phase IE 值填入该信息元素。 此参数配置一个相对于网络子系统本地时钟（Local Clock）、纳秒分辨率（Nanosecond Resolution）的时间点，表示预期在本地天线处发送 TX 帧帧起始定界符（SFD）末尾的时刻，等价于同步头（SHR）末尾、物理层头部（PHR）起始的时刻。 需要 IEEE802154_OPENTHREAD_HW_CST 能力（Capability）。 |

<a id="a80bc0d04ae7e2286abe372df49880ac8"></a>

### `ieee802154_openthread_hw_caps`

```c
enum ieee802154_openthread_hw_caps
```

ieee802154 驱动的 OpenThread 专用能力（Capabilities）。

此类型扩展 ieee802154_hw_caps。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `IEEE802154_OPENTHREAD_HW_MULTIPLE_CCA` | 支持采用 IEEE802154_OPENTHREAD_TX_MODE_TXTIME_MULTIPLE_CCA 模式发送的能力（Capability）。 |
| `IEEE802154_OPENTHREAD_HW_CST` | 支持 CST 相关特性的能力（Capability）。 CST 相关特性由 2024 年 7 月 11 日的《Thread-in-Mobile 规范变更》（Specification changes for Thread-in-Mobile）草案第 1 版描述。CST 允许按照该规范变更第 4.6.6.1 章发送包含 CST Phase 和 CST Period 信息元素（IEs）的帧。上层实现（OpenThread）负责准备待发送帧，并为 CST Phase 和 CST Period 预留占位位置；驱动实现负责根据配置参数 IEEE802154_OPENTHREAD_CONFIG_CST_PERIOD 和 IEEE802154_OPENTHREAD_CONFIG_EXPECTED_TX_TIME，为这两个信息元素填入正确值。 注意（Note）：CST 发送的设计与 CSL 接收非常相似。在 CSL 接收中，接收方通知对端自己能够接收的时间点；在 CST 发送中，发送方通知对端下一次发送发生的时间点。 |

**说明（Note）**：注意（Note）：CST 发送的设计与 CSL 接收非常相似。在 CSL 接收中，接收方通知对端自己能够接收的时间点；在 CST 发送中，发送方通知对端下一次发送发生的时间点。

<a id="a038a7e158a73533b1fd55bb92e5fa64a"></a>

### `ieee802154_openthread_tx_mode`

```c
enum ieee802154_openthread_tx_mode
```

发送模式（TX Mode）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `IEEE802154_OPENTHREAD_TX_MODE_TXTIME_MULTIPLE_CCA` | IEEE802154_OPENTHREAD_TX_MODE_TXTIME_MULTIPLE_CCA 模式允许发送已调度的数据包：在最多 1 + max_extra_cca_attempts 次背靠背执行的空闲信道评估（CCAs）之后，只要报告信道空闲即可发送。 此模式是非标准的 OpenThread 实验性特性（Experimental Feature），允许在指定时间窗口内发送数据包。最早发送时间的规定与其他 TXTIME 模式相同：第一次 CCA 报告信道空闲时，数据包 PHR 的第一个符号必须（SHALL）在调度的 TX 时间戳所表示的时刻出现在本地天线处，以下将该时刻称为 T_tx。 如果第一次 CCA 报告信道忙碌，则最多再执行 max_extra_cca_attempts 次 CCA，直到某次报告空闲并发送数据包；达到最大尝试次数仍未成功时，发送失败。 这些额外 CCA 的时序取决于驱动能力，驱动通过 T_recca 和 T_ccatx 属性报告它们，参见 IEEE802154_OPENTHREAD_ATTR_T_RECCA 和 IEEE802154_OPENTHREAD_ATTR_T_CCATX。根据这些属性，上层可以计算调度数据包 PHR 的第一个符号必须（SHALL）出现在本地天线处的最晚时间点 T_txmax： 最大发送延迟（T_maxtxdelay）和最晚发送时刻（T_txmax）：

`T_maxtxdelay = max_extra_cca_attempts * (aCcaTime + T_recca) - T_recca + T_ccatx`

`T_txmax = T_tx + T_maxtxdelay` aCcaTime 的定义参见 IEEE 802.15.4-2020 第 11.3 节表 11-1。 实现此发送模式（TX Mode）的驱动应当（SHOULD）尽量缩短 T_recca 和 T_ccatx。T_ccatx 必须（SHALL）小于或等于同一标准第 11.3 节表 11-1 定义的 aTurnaroundTime。 必须（SHALL）按照 phyCcaMode PHY PIB 属性的定义执行 CCA；参见同一标准第 11.3 节表 11-2。 需要 IEEE802154_OPENTHREAD_HW_MULTIPLE_CCA 能力（Capability）。 注意（Note）：IEEE802154_HW_SELECTIVE_TXCHANNEL 能力的适用方式与 IEEE802154_TX_MODE_TXTIME_CCA 相同。 |

**说明（Note）**：注意（Note）：IEEE802154_HW_SELECTIVE_TXCHANNEL 能力的适用方式与 IEEE802154_TX_MODE_TXTIME_CCA 相同。


## 5.5\_原页交叉引用（Cross References）

- [ieee802154_radio.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio_8h.html)
- [zephyr/net/ieee802154_radio.h](../api_source_network_reference/P010_ieee802154_radio.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P340_ieee802154_radio_openthread.h_源码浏览.md)
- [ieee802154_openthread_config](../network_core_model_reference/P037_ieee802154_openthread_config_结构体.md)
- [ieee802154_openthread_attr_value](../network_core_model_reference/P036_ieee802154_openthread_attr_value_结构体.md)
- [IEEE802154_HW_CAPS_BITS_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga40912ccb268768b4e96ce9cad35476af)
- [ieee802154_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf4deddd3f23ebfd65fa47c5d62634430)
- [ieee802154_config_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga34aecc5996174a812b295a3a4693ad09)
- [ieee802154_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf99cda89c29df3c0088fc57ec09cbcd4)
- [IEEE802154_HW_SELECTIVE_TXCHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4ab6cf4f3552d6193027a538a13b95952e)
- [IEEE802154_TX_MODE_TXTIME_CCA](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225da42b4589afb2180fde053fdbbf58c0d3e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a15a4b5a53be4b2c867eb9551de7d914aa4d92697c08b14201465db37b302c2fa5"></a>
<a id="a15a4b5a53be4b2c867eb9551de7d914aa0e68340300b0e2d29811289fa7c1987b"></a>
<a id="ab11e7d5ec46577a0259d68349ac19525ac06ead66659fa9a736d368a9d255bc95"></a>
<a id="ab11e7d5ec46577a0259d68349ac19525a2b1436aa0d7fdded8fda38b4ee8f2af7"></a>
<a id="ab11e7d5ec46577a0259d68349ac19525a7ee21cd052527506e860b4a3bc772a04"></a>
<a id="a80bc0d04ae7e2286abe372df49880ac8a9a1663d68026c5156a0f127ae086adc8"></a>
<a id="a80bc0d04ae7e2286abe372df49880ac8a8cd0cafed5d27222aff18e42b1693c7f"></a>
<a id="a038a7e158a73533b1fd55bb92e5fa64aa75f9fb57cf10207c5142a86552cb401f"></a>

---

[上一章](P004_zephyr__bluetooth__classic__hfp_hf.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__drivers__interrupt_controller__intc_esp32.h_文件参考.md)
