---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-67
title: bt_mesh_health_srv_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__srv__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_bt\_mesh\_health\_srv\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__srv__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

健康服务器（Health Server）模型的回调函数。

```c
#include <zephyr/bluetooth/mesh/health_srv.h>
```

<a id="details"></a>

健康服务器（Health Server）模型的回调函数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 67.1\_数据成员（Data Fields）

<a id="r_a03ff8869793804dd5943f5d2cd63cc3e"></a>

```c
int(* fault_get_cur )(const struct bt_mesh_model *model, uint8_t *test_id, uint16_t *company_id, uint8_t *faults, uint8_t *fault_count)
```

相关声明：[fault_get_cur](#a03ff8869793804dd5943f5d2cd63cc3e)、[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取当前故障的回调（Current faults callback）。

<a id="r_a555711f2892d8e5a96661c6fff03c7f8"></a>

```c
int(* fault_get_reg )(const struct bt_mesh_model *model, uint16_t company_id, uint8_t *test_id, uint8_t *faults, uint8_t *fault_count)
```

相关声明：[fault_get_reg](#a555711f2892d8e5a96661c6fff03c7f8)、[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取所有已登记故障的回调（Registered faults callback）。

<a id="r_afdc878362b78ccfeb4473bcdfb02b9d1"></a>

```c
int(* fault_clear )(const struct bt_mesh_model *model, uint16_t company_id)
```

相关声明：[fault_clear](#afdc878362b78ccfeb4473bcdfb02b9d1)、[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

清除与指定公司标识符（Company ID）关联的全部已登记故障（Registered faults）。

<a id="r_ab426938525f8478ab27dc08a2f25273f"></a>

```c
int(* fault_test )(const struct bt_mesh_model *model, uint8_t test_id, uint16_t company_id)
```

相关声明：[fault_test](#ab426938525f8478ab27dc08a2f25273f)、[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

运行自检（Self-test）。

<a id="r_ad9e8a392943d4848190c4513327bc52c"></a>

```c
void(* attn_on )(const struct bt_mesh_model *model)
```

相关声明：[attn_on](#ad9e8a392943d4848190c4513327bc52c)、[bt_mesh_model](P075_bt_mesh_model_结构体.md)。

开始让设备引起关注（Attention）。

<a id="r_abd881db6cf849433808bc6464e109b60"></a>

```c
void(* attn_off )(const struct bt_mesh_model *model)
```

相关声明：[attn_off](#abd881db6cf849433808bc6464e109b60)、[bt_mesh_model](P075_bt_mesh_model_结构体.md)。

停止关注状态（Attention state）。

## 67.2\_详细说明（Detailed Documentation）

<a id="abd881db6cf849433808bc6464e109b60"></a>

### `attn_off`

```c
void(* bt_mesh_health_srv_cb::attn_off) (const struct bt_mesh_model *model)
```

停止关注状态（Attention state）。

应停止此前为使设备引起关注（Attention）而启动的所有物理动作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `model` |  |

<a id="ad9e8a392943d4848190c4513327bc52c"></a>

### `attn_on`

```c
void(* bt_mesh_health_srv_cb::attn_on) (const struct bt_mesh_model *model)
```

开始让设备引起关注（Attention）。

关注状态（Attention state）用于将元素地址（Element address）对应到物理设备。调用此回调时，设备应启动能引起注意的物理过程，例如闪烁、蜂鸣、振动或移动。如果设备上有多个健康服务器实例（Health server instances），关注状态还应帮助识别服务器所在的具体元素。

引起关注的行为（Attention calling behavior）应持续到调用 `attn_off` 回调为止。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `model` | 要启动关注状态（Attention state）的健康服务器模型（Health Server model）。 |

<a id="afdc878362b78ccfeb4473bcdfb02b9d1"></a>

### `fault_clear`

```c
int(* bt_mesh_health_srv_cb::fault_clear) (const struct bt_mesh_model *model, uint16_t company_id)
```

清除与指定公司标识符（Company ID）关联的全部已登记故障（Registered faults）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `model` | 要清除故障的健康服务器模型实例（Health Server model instance）。 |
| `company_id` | 要清除其故障的公司标识符（Company ID）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="a03ff8869793804dd5943f5d2cd63cc3e"></a>

### `fault_get_cur`

```c
int(* bt_mesh_health_srv_cb::fault_get_cur) (const struct bt_mesh_model *model, uint8_t *test_id, uint16_t *company_id, uint8_t *faults, uint8_t *fault_count)
```

获取当前故障的回调（Current faults callback）。

故障值（Fault values）可以由规范定义，也可以由厂商定义。厂商专用故障（Vendor specific faults）应结合随附的公司标识符（Company ID）解释。规范定义的故障可针对任意公司标识符报告，同一故障也可针对多个公司标识符呈现。

所有故障都必须至少关联一个公司标识符（Company ID），代表设备厂商，或代表其专用故障值被使用的其他厂商。

如果多个公司标识符（Company IDs）都有活动故障，每次只返回与其中一个公司标识符关联的故障。若要报告多个公司标识符的故障，应在各次调用中交替选择要报告的公司标识符。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `model` | 要获取其故障的健康服务器模型实例（Health Server model instance）。 |
| `test_id` | 测试标识符响应缓冲区（Test ID response buffer）。 |
| `company_id` | 公司标识符响应缓冲区（Company ID response buffer）。 |
| `faults` | 要填入当前故障（Current faults）的数组。 |
| `fault_count` | 故障数组（Fault array）可容纳的故障数量。应更新此值，使其反映实际复制到数组中的故障数量。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="a555711f2892d8e5a96661c6fff03c7f8"></a>

### `fault_get_reg`

```c
int(* bt_mesh_health_srv_cb::fault_get_reg) (const struct bt_mesh_model *model, uint16_t company_id, uint8_t *test_id, uint8_t *faults, uint8_t *fault_count)
```

获取所有已登记故障的回调（Registered faults callback）。

已登记故障（Registered faults）包含上次调用 `fault_clear` 以来的全部历史故障和当前故障。只应报告与指定公司标识符（Company ID）关联的故障。

故障值（Fault values）可以由规范定义，也可以由厂商定义。厂商专用故障（Vendor specific faults）应结合随附的公司标识符（Company ID）解释。规范定义的故障可针对任意公司标识符报告，同一故障也可针对多个公司标识符呈现。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `model` | 要获取其故障的健康服务器模型实例（Health Server model instance）。 |
| `company_id` | 要获取其故障的公司标识符（Company ID）。 |
| `test_id` | 测试标识符响应缓冲区（Test ID response buffer）。 |
| `faults` | 要填入已登记故障（Registered faults）的数组。 |
| `fault_count` | 故障数组（Fault array）可容纳的故障数量。应更新此值，使其反映实际复制到数组中的故障数量。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ab426938525f8478ab27dc08a2f25273f"></a>

### `fault_test`

```c
int(* bt_mesh_health_srv_cb::fault_test) (const struct bt_mesh_model *model, uint8_t test_id, uint16_t company_id)
```

运行自检（Self-test）。

健康服务器（Health server）针对每个公司标识符（Company ID）最多可支持 256 项自检（Self-tests）。所有测试标识符（Test IDs）的行为均由厂商定义，应依据随附的公司标识符解释。测试失败应引起故障数组（Fault array）变化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `model` | 要执行测试的健康服务器模型实例（Health Server model instance）。 |
| `test_id` | 要执行的测试标识符（Test ID）。 |
| `company_id` | 执行测试所针对的公司标识符（Company ID）。 |

**返回（Returns）**：返回值（Returns）：成功启动测试执行时为 `0`，否则返回负错误码。注意，若测试未能启动，故障数组（Fault array）不会报告给客户端。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/health_srv.h`

## 67.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/health_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/health__srv_8h_source.html)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P066_bt_mesh_health_srv_结构体.md) · [返回大纲](大纲.md) · [下一章](P068_bt_mesh_key_结构体.md)
