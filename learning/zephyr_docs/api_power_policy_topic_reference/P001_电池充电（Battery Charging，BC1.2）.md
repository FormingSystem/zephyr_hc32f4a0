---
id: learning.zephyr-docs.api-power-policy-topic-reference.page-1
title: 电池充电（Battery Charging，BC1.2）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_电池充电（Battery Charging，BC1.2）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB 电池充电（Battery Charging，BC1.2）驱动 API。

<a id="details"></a>

USB 电池充电（Battery Charging，BC1.2）驱动 API。

<a id="header-groups"></a>
<a id="groups"></a>

## 1.1\_主题（Topics）

<a id="r_b12_5Femulator_5Fbackend"></a>

相关声明：[BC1.2 仿真器支持 API（原文：BC1.2 backed emulator APIs）](../hardware/P491_BC1点2仿真后端接口.md)。

BC1.2 仿真器后端 API（BC1.2 backend emulator APIs）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.2\_数据结构（Data Structures）

<a id="r_bc12_5Fpartner_5Fstate"></a>

```c
struct bc12_partner_state
```

相关声明：[bc12_partner_state](../driver_model_reference/P025_BC12伙伴状态.md)。

电池充电规范 1.2（Battery Charging 1.2，BC1.2）检测到的伙伴状态（Partner State）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_gaeb039486c7826fe493e7f402212f2661"></a>

```c
typedef void(* bc12_callback_t) (const struct device *dev, struct bc12_partner_state *state, void *user_data)
```

相关声明：[bc12_callback_t](#gaeb039486c7826fe493e7f402212f2661)、[device](../device_reference/P002_设备对象结构.md)、[bc12_partner_state](../driver_model_reference/P025_BC12伙伴状态.md)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

用于充电器配置（Charger Configuration）的 BC1.2 回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.4\_枚举（Enumerations）

<a id="r_ga035f4e4ba27f76094145571ebea97d73"></a>

```c
enum bc12_role { BC12_DISCONNECTED , BC12_PORTABLE_DEVICE , BC12_CHARGING_PORT }
```

相关声明：[bc12_role](#ga035f4e4ba27f76094145571ebea97d73)、[BC12_DISCONNECTED](#gga035f4e4ba27f76094145571ebea97d73a376830bcd04da44b9a2215a6f10dcf22)、[BC12_PORTABLE_DEVICE](#gga035f4e4ba27f76094145571ebea97d73a8be0fd9ef5bc456b25964367388e3e48)、[BC12_CHARGING_PORT](#gga035f4e4ba27f76094145571ebea97d73a2d7dffa7a9a134e55d48bf3c699d96ef)。

BC1.2 设备角色（Device Role）。

<a id="r_ga9ae800d490c2cbd3234a81c503649bdb"></a>

```c
enum bc12_type { BC12_TYPE_NONE , BC12_TYPE_SDP , BC12_TYPE_DCP , BC12_TYPE_CDP , BC12_TYPE_PROPRIETARY , BC12_TYPE_UNKNOWN , BC12_TYPE_COUNT }
```

相关声明：[bc12_type](#ga9ae800d490c2cbd3234a81c503649bdb)、[BC12_TYPE_NONE](#gga9ae800d490c2cbd3234a81c503649bdba55bff2c1d47018dc7d175c178c6eefe6)、[BC12_TYPE_SDP](#gga9ae800d490c2cbd3234a81c503649bdba4109f85b375b5dbfd2eada250fc06425)、[BC12_TYPE_DCP](#gga9ae800d490c2cbd3234a81c503649bdba6ad9973121a077d239f8db7ecd7b76f3)、[BC12_TYPE_CDP](#gga9ae800d490c2cbd3234a81c503649bdba2b231ba4723445006b5993431064eb9c)、[BC12_TYPE_PROPRIETARY](#gga9ae800d490c2cbd3234a81c503649bdba08527a826ab4639e4e6a72dc54c51bb2)、[BC12_TYPE_UNKNOWN](#gga9ae800d490c2cbd3234a81c503649bdba25c692e9f22c761de33f738e08bf4e30)、[BC12_TYPE_COUNT](#gga9ae800d490c2cbd3234a81c503649bdba672c2ed7c64ca4f13e1eb96456585d50)。

BC1.2 充电对端类型（Charging Partner Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.5\_函数（Functions）

<a id="r_ga2a879017d34392308d4c078178db8407"></a>

```c
int bc12_set_role (const struct device *dev, enum bc12_role role)
```

相关声明：[bc12_set_role](#ga2a879017d34392308d4c078178db8407)、[device](../device_reference/P002_设备对象结构.md)、[bc12_role](#ga035f4e4ba27f76094145571ebea97d73)。

设置 BC1.2 角色（Role）。

<a id="r_ga0db43c4cc595cb76738cf24d97fa5228"></a>

```c
int bc12_set_result_cb (const struct device *dev, bc12_callback_t cb, void *user_data)
```

相关声明：[bc12_set_result_cb](#ga0db43c4cc595cb76738cf24d97fa5228)、[device](../device_reference/P002_设备对象结构.md)、[bc12_callback_t](#gaeb039486c7826fe493e7f402212f2661)。

注册 BC1.2 结果回调（Callback）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 1.6\_BC1.2 常量（Constants）

<a id="r_gae32f7af00346f7baf968287eb874d880"></a>

```c
#define BC12_CHARGER_VOLTAGE_UV 5000 * 1000
```

相关声明：[BC12_CHARGER_VOLTAGE_UV](#gae32f7af00346f7baf968287eb874d880)。

BC1.2 USB 充电器电压（Charger Voltage）。

<a id="r_ga5ebbce02f5cb47de4565ef17d57ca25a"></a>

```c
#define BC12_CHARGER_MIN_CURR_UA 2500
```

相关声明：[BC12_CHARGER_MIN_CURR_UA](#ga5ebbce02f5cb47de4565ef17d57ca25a)。

BC1.2 USB 充电器最小电流（Minimum Current）。

<a id="r_gaa327167a6bb6ee0c44b98faab708d1f2"></a>

```c
#define BC12_CHARGER_MAX_CURR_UA 1500 * 1000
```

相关声明：[BC12_CHARGER_MAX_CURR_UA](#gaa327167a6bb6ee0c44b98faab708d1f2)。

BC1.2 USB 充电器最大电流（Maximum Current）。

## 1.7\_详细说明（Detailed Documentation）

<a id="gaa327167a6bb6ee0c44b98faab708d1f2"></a>

### `BC12_CHARGER_MAX_CURR_UA`

```c
#define BC12_CHARGER_MAX_CURR_UA 1500 * 1000
```

```c
#include <zephyr/drivers/usb/usb_bc12.h>
```

BC1.2 USB 充电器最大电流（Maximum Current）。

<a id="ga5ebbce02f5cb47de4565ef17d57ca25a"></a>

### `BC12_CHARGER_MIN_CURR_UA`

```c
#define BC12_CHARGER_MIN_CURR_UA 2500
```

```c
#include <zephyr/drivers/usb/usb_bc12.h>
```

BC1.2 USB 充电器最小电流（Minimum Current）。

设为与挂起电流（Isusp）2.5 mA 参数一致的值。BC1.2 检测失败，或连接的对端为标准下行端口（Standard Downstream Port，SDP）时，驱动返回此值。

应用可以在确定 USB 设备状态为挂起／未配置／已配置（Suspended/Unconfigured/Configured）之后增加取用电流。挂起：2.5 mA；未配置：100 mA；已配置：500 mA（USB 2.0）。

<a id="gae32f7af00346f7baf968287eb874d880"></a>

### `BC12_CHARGER_VOLTAGE_UV`

```c
#define BC12_CHARGER_VOLTAGE_UV 5000 * 1000
```

```c
#include <zephyr/drivers/usb/usb_bc12.h>
```

BC1.2 USB 充电器电压（Charger Voltage）。

<a id="gaeb039486c7826fe493e7f402212f2661"></a>

### `bc12_callback_t`

```c
typedef void(* bc12_callback_t) (const struct device *dev, struct bc12_partner_state *state, void *user_data)
```

```c
#include <zephyr/drivers/usb/usb_bc12.h>
```

用于充电器配置（Charger Configuration）的 BC1.2 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 正在通知新充电器状态（Charger State）的 BC1.2 设备。 |
| `state` | BC1.2 客户端当前状态（Client State），包括检测到的 BC1.2 类型、电压和电流限制。若为 `NULL`，表示对端充电器已断开，或 BC1.2 设备工作在主机模式（Host Mode）。 |
| `user_data` | 请求方提供并传递给回调（Callback）的数据。 |

<a id="ga035f4e4ba27f76094145571ebea97d73"></a>

### `bc12_role`

```c
enum bc12_role
```

```c
#include <zephyr/drivers/usb/usb_bc12.h>
```

BC1.2 设备角色（Device Role）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BC12_DISCONNECTED` | 未连接 BC1.2 设备（Device）。 |
| `BC12_PORTABLE_DEVICE` | BC1.2 设备为便携设备（Portable Device）。 |
| `BC12_CHARGING_PORT` | BC1.2 设备为充电端口（Charging Port）。 |

<a id="ga9ae800d490c2cbd3234a81c503649bdb"></a>

### `bc12_type`

```c
enum bc12_type
```

```c
#include <zephyr/drivers/usb/usb_bc12.h>
```

BC1.2 充电对端类型（Charging Partner Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BC12_TYPE_NONE` | 未连接对端（Partner）。 |
| `BC12_TYPE_SDP` | 标准下行端口（Standard Downstream Port，SDP）。 |
| `BC12_TYPE_DCP` | 专用充电端口（Dedicated Charging Port，DCP）。 |
| `BC12_TYPE_CDP` | 充电下行端口（Charging Downstream Port，CDP）。 |
| `BC12_TYPE_PROPRIETARY` | 专有充电端口（Proprietary Charging Port）。 |
| `BC12_TYPE_UNKNOWN` | 未知充电端口（Unknown Charging Port），BC1.2 检测失败。 |
| `BC12_TYPE_COUNT` | 有效 BC12 类型（Types）的数量。 |

<a id="ga0db43c4cc595cb76738cf24d97fa5228"></a>

### `bc12_set_result_cb()`

```c
int bc12_set_result_cb ( const struct device * dev, bc12_callback_t cb, void * user_data )
```

```c
#include <zephyr/drivers/usb/usb_bc12.h>
```

注册 BC1.2 结果回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 BC1.2 驱动实例的设备结构体（Device Structure）的指针。 |
| `cb` | 结果回调（Result Callback）的函数指针。 |
| `user_data` | 请求方提供并传递给回调（Callback）的数据。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 一般输入／输出错误（Input/Output Error）。 |

<a id="ga2a879017d34392308d4c078178db8407"></a>

### `bc12_set_role()`

```c
int bc12_set_role ( const struct device * dev, enum bc12_role role )
```

```c
#include <zephyr/drivers/usb/usb_bc12.h>
```

设置 BC1.2 角色（Role）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 BC1.2 驱动实例的设备结构体（Device Structure）的指针。 |
| `role` | BC1.2 设备的新角色（New Role）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 一般输入／输出错误（Input/Output Error）。 |


## 1.8\_原页交叉引用（Cross References）

- [BC1.2 仿真器支持 API（原文：BC1.2 backed emulator APIs）](../hardware/P491_BC1点2仿真后端接口.md)
- [bc12_partner_state](../driver_model_reference/P025_BC12伙伴状态.md)
- [device](../device_reference/P002_设备对象结构.md)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [zephyr/drivers/usb/usb_bc12.h](../api_file_service_interface_reference/P054_zephyr__drivers__usb__usb_bc12.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga035f4e4ba27f76094145571ebea97d73a376830bcd04da44b9a2215a6f10dcf22"></a>
<a id="gga035f4e4ba27f76094145571ebea97d73a8be0fd9ef5bc456b25964367388e3e48"></a>
<a id="gga035f4e4ba27f76094145571ebea97d73a2d7dffa7a9a134e55d48bf3c699d96ef"></a>
<a id="gga9ae800d490c2cbd3234a81c503649bdba55bff2c1d47018dc7d175c178c6eefe6"></a>
<a id="gga9ae800d490c2cbd3234a81c503649bdba4109f85b375b5dbfd2eada250fc06425"></a>
<a id="gga9ae800d490c2cbd3234a81c503649bdba6ad9973121a077d239f8db7ecd7b76f3"></a>
<a id="gga9ae800d490c2cbd3234a81c503649bdba2b231ba4723445006b5993431064eb9c"></a>
<a id="gga9ae800d490c2cbd3234a81c503649bdba08527a826ab4639e4e6a72dc54c51bb2"></a>
<a id="gga9ae800d490c2cbd3234a81c503649bdba25c692e9f22c761de33f738e08bf4e30"></a>
<a id="gga9ae800d490c2cbd3234a81c503649bdba672c2ed7c64ca4f13e1eb96456585d50"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_游戏音频配置文件（Gaming Audio Profile，GMAP）的 LC3 预设.md)
