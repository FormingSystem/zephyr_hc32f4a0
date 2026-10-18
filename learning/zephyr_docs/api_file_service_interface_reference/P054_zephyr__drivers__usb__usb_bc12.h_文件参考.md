---
id: learning.zephyr-docs.api-file-service-interface-reference.page-54
title: zephyr__drivers__usb__usb_bc12.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__bc12_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_zephyr\_\_drivers\_\_usb\_\_usb\_bc12.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usb__bc12_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB BC1.2电池充电检测（Battery Charging Detect）驱动的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/syscalls/usb_bc12.h>
```

查看此文件的源码。

USB BC1.2电池充电检测（Battery Charging Detect）驱动的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 54.1\_数据结构（Data Structures）

<a id="r_bc12_5Fpartner_5Fstate"></a>

```c
struct bc12_partner_state
```

相关声明：[bc12_partner_state](../driver_model_reference/P025_BC12伙伴状态.md)。

电池充电规范 1.2（Battery Charging 1.2，BC1.2）检测到的伙伴状态（Partner State）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 54.2\_宏定义（Macros）

<a id="define-members-0"></a>

### BC1.2 常量（Constants）

<a id="r_gae32f7af00346f7baf968287eb874d880"></a>

```c
#define BC12_CHARGER_VOLTAGE_UV 5000 * 1000
```

相关声明：[BC12_CHARGER_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gae32f7af00346f7baf968287eb874d880)。

BC1.2 USB 充电器电压（Charger Voltage）。

<a id="r_ga5ebbce02f5cb47de4565ef17d57ca25a"></a>

```c
#define BC12_CHARGER_MIN_CURR_UA 2500
```

相关声明：[BC12_CHARGER_MIN_CURR_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga5ebbce02f5cb47de4565ef17d57ca25a)。

BC1.2 USB 充电器最小电流（Minimum Current）。

<a id="r_gaa327167a6bb6ee0c44b98faab708d1f2"></a>

```c
#define BC12_CHARGER_MAX_CURR_UA 1500 * 1000
```

相关声明：[BC12_CHARGER_MAX_CURR_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gaa327167a6bb6ee0c44b98faab708d1f2)。

BC1.2 USB 充电器最大电流（Maximum Current）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 54.3\_类型定义（Typedefs）

<a id="r_gaeb039486c7826fe493e7f402212f2661"></a>

```c
typedef void(* bc12_callback_t) (const struct device *dev, struct bc12_partner_state *state, void *user_data)
```

相关声明：[bc12_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gaeb039486c7826fe493e7f402212f2661)、[device](../device_reference/P002_设备对象结构.md)、[bc12_partner_state](../driver_model_reference/P025_BC12伙伴状态.md)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

用于充电器配置（Charger Configuration）的 BC1.2 回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 54.4\_枚举（Enumerations）

<a id="r_ga035f4e4ba27f76094145571ebea97d73"></a>

```c
enum bc12_role { BC12_DISCONNECTED , BC12_PORTABLE_DEVICE , BC12_CHARGING_PORT }
```

相关声明：[bc12_role](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga035f4e4ba27f76094145571ebea97d73)、[BC12_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga035f4e4ba27f76094145571ebea97d73a376830bcd04da44b9a2215a6f10dcf22)、[BC12_PORTABLE_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga035f4e4ba27f76094145571ebea97d73a8be0fd9ef5bc456b25964367388e3e48)、[BC12_CHARGING_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga035f4e4ba27f76094145571ebea97d73a2d7dffa7a9a134e55d48bf3c699d96ef)。

BC1.2 设备角色（Device Role）。

<a id="r_ga9ae800d490c2cbd3234a81c503649bdb"></a>

```c
enum bc12_type { BC12_TYPE_NONE , BC12_TYPE_SDP , BC12_TYPE_DCP , BC12_TYPE_CDP , BC12_TYPE_PROPRIETARY , BC12_TYPE_UNKNOWN , BC12_TYPE_COUNT }
```

相关声明：[bc12_type](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga9ae800d490c2cbd3234a81c503649bdb)、[BC12_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba55bff2c1d47018dc7d175c178c6eefe6)、[BC12_TYPE_SDP](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba4109f85b375b5dbfd2eada250fc06425)、[BC12_TYPE_DCP](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba6ad9973121a077d239f8db7ecd7b76f3)、[BC12_TYPE_CDP](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba2b231ba4723445006b5993431064eb9c)、[BC12_TYPE_PROPRIETARY](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba08527a826ab4639e4e6a72dc54c51bb2)、[BC12_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba25c692e9f22c761de33f738e08bf4e30)、[BC12_TYPE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba672c2ed7c64ca4f13e1eb96456585d50)。

BC1.2 充电对端类型（Charging Partner Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 54.5\_函数（Functions）

<a id="r_ga2a879017d34392308d4c078178db8407"></a>

```c
int bc12_set_role (const struct device *dev, enum bc12_role role)
```

相关声明：[bc12_set_role](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga2a879017d34392308d4c078178db8407)、[device](../device_reference/P002_设备对象结构.md)、[bc12_role](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga035f4e4ba27f76094145571ebea97d73)。

设置 BC1.2 角色（Role）。

<a id="r_ga0db43c4cc595cb76738cf24d97fa5228"></a>

```c
int bc12_set_result_cb (const struct device *dev, bc12_callback_t cb, void *user_data)
```

相关声明：[bc12_set_result_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga0db43c4cc595cb76738cf24d97fa5228)、[device](../device_reference/P002_设备对象结构.md)、[bc12_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gaeb039486c7826fe493e7f402212f2661)。

注册 BC1.2 结果回调（Callback）。


## 54.6\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P235_usb_bc12.h_源码浏览.md)
- [bc12_partner_state](../driver_model_reference/P025_BC12伙伴状态.md)
- [BC12_CHARGER_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gae32f7af00346f7baf968287eb874d880)
- [BC12_CHARGER_MIN_CURR_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga5ebbce02f5cb47de4565ef17d57ca25a)
- [BC12_CHARGER_MAX_CURR_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gaa327167a6bb6ee0c44b98faab708d1f2)
- [bc12_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gaeb039486c7826fe493e7f402212f2661)
- [device](../device_reference/P002_设备对象结构.md)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [bc12_role](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga035f4e4ba27f76094145571ebea97d73)
- [BC12_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga035f4e4ba27f76094145571ebea97d73a376830bcd04da44b9a2215a6f10dcf22)
- [BC12_PORTABLE_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga035f4e4ba27f76094145571ebea97d73a8be0fd9ef5bc456b25964367388e3e48)
- [BC12_CHARGING_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga035f4e4ba27f76094145571ebea97d73a2d7dffa7a9a134e55d48bf3c699d96ef)
- [bc12_type](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga9ae800d490c2cbd3234a81c503649bdb)
- [BC12_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba55bff2c1d47018dc7d175c178c6eefe6)
- [BC12_TYPE_SDP](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba4109f85b375b5dbfd2eada250fc06425)
- [BC12_TYPE_DCP](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba6ad9973121a077d239f8db7ecd7b76f3)
- [BC12_TYPE_CDP](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba2b231ba4723445006b5993431064eb9c)
- [BC12_TYPE_PROPRIETARY](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba08527a826ab4639e4e6a72dc54c51bb2)
- [BC12_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba25c692e9f22c761de33f738e08bf4e30)
- [BC12_TYPE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#gga9ae800d490c2cbd3234a81c503649bdba672c2ed7c64ca4f13e1eb96456585d50)
- [bc12_set_role](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga2a879017d34392308d4c078178db8407)
- [bc12_set_result_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga0db43c4cc595cb76738cf24d97fa5228)

<a id="header-details"></a>

---

[上一章](P053_zephyr__net__trickle.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P055_zephyr__modem__at__user_pipe.h_文件参考.md)
