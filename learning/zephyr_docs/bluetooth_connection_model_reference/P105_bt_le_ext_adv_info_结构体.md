---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-105
title: bt_le_ext_adv_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__ext__adv__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第105章\_bt\_le\_ext\_adv\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__ext__adv__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

广播集（Advertising Set）的信息结构。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

广播集（Advertising Set）的信息结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 105.1\_数据成员（Data Fields）

<a id="r_a06aa727cd2523914bc7509713585bffd"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#a06aa727cd2523914bc7509713585bffd)。

本地身份句柄（Local identity handle）。

<a id="r_a485e4a8124fddee897fe744836cbfb24"></a>

```c
int8_t tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power](#a485e4a8124fddee897fe744836cbfb24)。

当前选定的发射功率（Transmit Power），单位为 dBm。

<a id="r_a19877c440137814ec0e4aa1a1270f6fe"></a>

```c
uint8_t sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sid](#a19877c440137814ec0e4aa1a1270f6fe)。

广播集标识符（Advertising Set ID）。

<a id="r_a0dd0aa8a26fe1ef5813fa07732c5c4c9"></a>

```c
const bt_addr_le_t * addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a0dd0aa8a26fe1ef5813fa07732c5c4c9)。

当前使用的本地广播地址（Local advertising address）。

<a id="r_a0ae2f62772732a6db460d4a0127dd17a"></a>

```c
enum bt_le_ext_adv_state ext_adv_state
```

相关声明：[bt_le_ext_adv_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga544ccde35638d8f580942d830fe9f242)、[ext_adv_state](#a0ae2f62772732a6db460d4a0127dd17a)。

扩展广播状态（Extended advertising state）。

<a id="r_ad802b5af32353d757a84e5039c973f3a"></a>

```c
enum bt_le_per_adv_state per_adv_state
```

相关声明：[bt_le_per_adv_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga6bb77c0808c761753650cde28ddb013e)、[per_adv_state](#ad802b5af32353d757a84e5039c973f3a)。

周期广播状态（Periodic advertising state）。

## 105.2\_详细说明（Detailed Documentation）

<a id="a0dd0aa8a26fe1ef5813fa07732c5c4c9"></a>

### `addr`

```c
const bt_addr_le_t* bt_le_ext_adv_info::addr
```

当前使用的本地广播地址（Local advertising address）。

广播集所使用的广播地址，可以是身份地址（Identity address）、静态随机地址（Static random address）、可解析私有地址（RPA）或不可解析私有地址（NRPA）。对于使用 RPA 的广播集，此处返回的是 RPA 本身，而非其解析得到的身份地址。此值在设置广播参数时确定，因此只有在 `bt_le_ext_adv_create()` 或 `bt_le_ext_adv_update_param()` 成功后才有意义；此前读取为 `BT_ADDR_LE_ANY`。

此指针的有效期与广播集对象（Advertising set object）相同，即持续到调用 `bt_le_ext_adv_delete()` 为止；重新配置和私有地址轮换时，它会跟随广播集更新。如果需要在更久之后使用该地址，应复制它。

**说明（Note）**：注意（Note）：若广播集被配置为让控制器根据其解析列表（Resolving list）解析地址，控制器可能替换为本地生成、主机无法观察到的可解析私有地址（RPA）。此时报告已配置的回退地址（Fallback address）。

<a id="a0ae2f62772732a6db460d4a0127dd17a"></a>

### `ext_adv_state`

```c
enum bt_le_ext_adv_state bt_le_ext_adv_info::ext_adv_state
```

扩展广播状态（Extended advertising state）。

<a id="a06aa727cd2523914bc7509713585bffd"></a>

### `id`

```c
uint8_t bt_le_ext_adv_info::id
```

本地身份句柄（Local identity handle）。

<a id="ad802b5af32353d757a84e5039c973f3a"></a>

### `per_adv_state`

```c
enum bt_le_per_adv_state bt_le_ext_adv_info::per_adv_state
```

周期广播状态（Periodic advertising state）。

<a id="a19877c440137814ec0e4aa1a1270f6fe"></a>

### `sid`

```c
uint8_t bt_le_ext_adv_info::sid
```

广播集标识符（Advertising Set ID）。

广播集配置时未使用 `BT_LE_ADV_OPT_EXT_ADV` 的情况下，值为 `BT_GAP_SID_INVALID`。

<a id="a485e4a8124fddee897fe744836cbfb24"></a>

### `tx_power`

```c
int8_t bt_le_ext_adv_info::tx_power
```

当前选定的发射功率（Transmit Power），单位为 dBm。

范围（Range）：-127 至 +20。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 105.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [bt_le_ext_adv_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga544ccde35638d8f580942d830fe9f242)
- [bt_le_per_adv_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga6bb77c0808c761753650cde28ddb013e)
- [bt_le_ext_adv_create()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad02b855dd7a26e3910b247fa73f19297)
- [bt_le_ext_adv_update_param()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1aabdb81cb1a1841ff0fb91d849123fc)
- [BT_ADDR_LE_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga17e9efacd50c682b2f709c217e920d48)
- [bt_le_ext_adv_delete()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga62310a27f7fea925dfcf3abd7c454787)
- [BT_GAP_SID_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga103af3e3142473be8897cd2647dca915)
- [BT_LE_ADV_OPT_EXT_ADV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ae33ae9d8e43cce82e47fa73999d415ab)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P104_bt_le_ext_adv_connected_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P106_bt_le_ext_adv_scanned_info_结构体.md)
