---
id: learning.zephyr-docs.network-service-model-reference.page-14
title: ethphy_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structethphy__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_ethphy\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structethphy__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：以太网物理层（Ethernet PHY）驱动操作。

```c
#include <zephyr/net/phy.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：以太网物理层（Ethernet PHY）驱动操作。这是每个以太网 PHY 驱动都需要定义的驱动 API 结构体，其中包含指向驱动所实现操作的函数指针，以及其他驱动专用常量数据。标记为 REQ 的成员必须由驱动设置，标记为 OPT 的成员为可选。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_aa205fb9e753f8a22118be14de07986ad"></a>

```c
int(* get_link )(const struct device *dev, struct phy_link_state *state)
```

相关声明：[get_link](#aa205fb9e753f8a22118be14de07986ad)、[device](../device_reference/P002_设备对象结构.md)、[phy_link_state](P040_phy_link_state_结构体.md)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)。

可选（OPT）：获取 PHY 链路状态。

<a id="r_a307ea6c0541ab578d8ff7ccf2027e0df"></a>

```c
int(* cfg_link )(const struct device *dev, enum phy_link_speed adv_speeds, enum phy_cfg_link_flag flags)
```

相关声明：[cfg_link](#a307ea6c0541ab578d8ff7ccf2027e0df)、[device](../device_reference/P002_设备对象结构.md)、[phy_link_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga9b97fff9fcd6823c9b564b3e86b8da68)、[phy_cfg_link_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga6221da76ffca235eafa291b90eab0d93)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

可选（OPT）：配置 PHY 链路。

<a id="r_ad28d8eedf15a1834492988f4586d7c35"></a>

```c
int(* link_cb_set )(const struct device *dev, phy_callback_t cb, void *user_data)
```

相关声明：[link_cb_set](#ad28d8eedf15a1834492988f4586d7c35)、[device](../device_reference/P002_设备对象结构.md)、[phy_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga3ee3db4ac48395f07d0de536b313dfa4)。

可选（OPT）：设置链路状态变化回调。

<a id="r_ace007566a66cc34fb72efa03698dbcf7"></a>

```c
int(* read )(const struct device *dev, uint16_t reg_addr, uint32_t *data)
```

相关声明：[read](#ace007566a66cc34fb72efa03698dbcf7)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

可选（OPT）：读取 PHY 寄存器。

<a id="r_a5f5dc34c75601974ae4046300e6acf85"></a>

```c
int(* write )(const struct device *dev, uint16_t reg_addr, uint32_t data)
```

相关声明：[write](#a5f5dc34c75601974ae4046300e6acf85)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

可选（OPT）：写入 PHY 寄存器。

<a id="r_a4fd123655cd1dc8ca6c650cf76f3589f"></a>

```c
int(* read_c45 )(const struct device *dev, uint8_t devad, uint16_t regad, uint16_t *data)
```

相关声明：[read_c45](#a4fd123655cd1dc8ca6c650cf76f3589f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

可选（OPT）：读取 PHY 第 45 条（C45）寄存器。

<a id="r_a1f66a4f770674baa32390c1f2e972694"></a>

```c
int(* write_c45 )(const struct device *dev, uint8_t devad, uint16_t regad, uint16_t data)
```

相关声明：[write_c45](#a1f66a4f770674baa32390c1f2e972694)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

可选（OPT）：写入 PHY 第 45 条（C45）寄存器。

<a id="r_a1f56afd3cfc34b759c604b55c11c6214"></a>

```c
int(* set_plca_cfg )(const struct device *dev, struct phy_plca_cfg *plca_cfg)
```

相关声明：[set_plca_cfg](#a1f56afd3cfc34b759c604b55c11c6214)、[device](../device_reference/P002_设备对象结构.md)、[phy_plca_cfg](P041_phy_plca_cfg_结构体.md)。

可选（OPT）：写入 PHY 物理层冲突避免（PLCA）配置。

<a id="r_a9b48f6b3e38da454f658cbcbbd40398c"></a>

```c
int(* get_plca_cfg )(const struct device *dev, struct phy_plca_cfg *plca_cfg)
```

相关声明：[get_plca_cfg](#a9b48f6b3e38da454f658cbcbbd40398c)、[device](../device_reference/P002_设备对象结构.md)、[phy_plca_cfg](P041_phy_plca_cfg_结构体.md)。

可选（OPT）：读取 PHY PLCA 配置。

<a id="r_a68af7c0c8d0e22243b745d09de1a5a47"></a>

```c
int(* get_plca_sts )(const struct device *dev, bool *plca_sts)
```

相关声明：[get_plca_sts](#a68af7c0c8d0e22243b745d09de1a5a47)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

可选（OPT）：读取 PHY PLCA 状态。

## 14.2\_详细说明（Detailed Documentation）

<a id="a307ea6c0541ab578d8ff7ccf2027e0df"></a>

### `cfg_link`

```c
int(* ethphy_driver_api::cfg_link) (const struct device *dev, enum phy_link_speed adv_speeds, enum phy_cfg_link_flag flags)
```

可选（OPT）：配置 PHY 链路。

<a id="aa205fb9e753f8a22118be14de07986ad"></a>

### `get_link`

```c
int(* ethphy_driver_api::get_link) (const struct device *dev, struct phy_link_state *state)
```

可选（OPT）：获取 PHY 链路状态。

<a id="a9b48f6b3e38da454f658cbcbbd40398c"></a>

### `get_plca_cfg`

```c
int(* ethphy_driver_api::get_plca_cfg) (const struct device *dev, struct phy_plca_cfg *plca_cfg)
```

可选（OPT）：读取 PHY PLCA 配置。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_ETH_PHY_API_PLCA`。

<a id="a68af7c0c8d0e22243b745d09de1a5a47"></a>

### `get_plca_sts`

```c
int(* ethphy_driver_api::get_plca_sts) (const struct device *dev, bool *plca_sts)
```

可选（OPT）：读取 PHY PLCA 状态。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_ETH_PHY_API_PLCA`。

<a id="ad28d8eedf15a1834492988f4586d7c35"></a>

### `link_cb_set`

```c
int(* ethphy_driver_api::link_cb_set) (const struct device *dev, phy_callback_t cb, void *user_data)
```

可选（OPT）：设置链路状态变化回调。

**说明（Note）**：重要：设置回调后，即使链路状态没有变化，驱动也必须调用一次该回调。

<a id="ace007566a66cc34fb72efa03698dbcf7"></a>

### `read`

```c
int(* ethphy_driver_api::read) (const struct device *dev, uint16_t reg_addr, uint32_t *data)
```

可选（OPT）：读取 PHY 寄存器。

<a id="a4fd123655cd1dc8ca6c650cf76f3589f"></a>

### `read_c45`

```c
int(* ethphy_driver_api::read_c45) (const struct device *dev, uint8_t devad, uint16_t regad, uint16_t *data)
```

可选（OPT）：读取 PHY 第 45 条（C45）寄存器。

<a id="a1f56afd3cfc34b759c604b55c11c6214"></a>

### `set_plca_cfg`

```c
int(* ethphy_driver_api::set_plca_cfg) (const struct device *dev, struct phy_plca_cfg *plca_cfg)
```

可选（OPT）：写入 PHY 物理层冲突避免（PLCA）配置。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_ETH_PHY_API_PLCA`。

<a id="a5f5dc34c75601974ae4046300e6acf85"></a>

### `write`

```c
int(* ethphy_driver_api::write) (const struct device *dev, uint16_t reg_addr, uint32_t data)
```

可选（OPT）：写入 PHY 寄存器。

<a id="a1f66a4f770674baa32390c1f2e972694"></a>

### `write_c45`

```c
int(* ethphy_driver_api::write_c45) (const struct device *dev, uint8_t devad, uint16_t regad, uint16_t data)
```

可选（OPT）：写入 PHY 第 45 条（C45）寄存器。

本数据类型文档由以下文件生成：

- `zephyr/net/phy.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/net/phy.h](https://docs.zephyrproject.org/latest/doxygen/html/phy_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [phy_link_state](P040_phy_link_state_结构体.md)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [phy_link_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga9b97fff9fcd6823c9b564b3e86b8da68)
- [phy_cfg_link_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga6221da76ffca235eafa291b90eab0d93)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [phy_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga3ee3db4ac48395f07d0de536b313dfa4)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [phy_plca_cfg](P041_phy_plca_cfg_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)
- [CONFIG_ETH_PHY_API_PLCA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_PHY_API_PLCA)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_ethernet_txtime_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_gptp_clk_src_time_invoke_params_结构体.md)
