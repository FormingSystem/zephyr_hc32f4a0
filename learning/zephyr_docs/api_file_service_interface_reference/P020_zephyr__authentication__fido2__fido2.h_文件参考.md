---
id: learning.zephyr-docs.api-file-service-interface-reference.page-20
title: zephyr__authentication__fido2__fido2.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fido2_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_zephyr\_\_authentication\_\_fido2\_\_fido2.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fido2_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FIDO2认证器（Authenticator）的公共API。

<a id="details"></a>

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

查看此文件的源码。

FIDO2认证器（Authenticator）的公共API。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 20.1\_类型定义（Typedefs）

<a id="r_gad0a191f4a48998fe857dc6315d225d94"></a>

```c
typedef void(* fido2_state_callback_t) (enum fido2_runtime_state state, void *user_data)
```

相关声明：[fido2_state_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gad0a191f4a48998fe857dc6315d225d94)、[fido2_runtime_state](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gabf5068079e94310fb4b942df56ec1d10)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

FIDO2 运行时状态回调（Runtime State Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 20.2\_枚举（Enumerations）

<a id="r_gabf5068079e94310fb4b942df56ec1d10"></a>

```c
enum fido2_runtime_state { FIDO2_RUNTIME_STATE_STOPPED = 0 , FIDO2_RUNTIME_STATE_IDLE , FIDO2_RUNTIME_STATE_WAITING_USER_PRESENCE , FIDO2_RUNTIME_STATE_PROCESSING }
```

相关声明：[fido2_runtime_state](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gabf5068079e94310fb4b942df56ec1d10)、[FIDO2_RUNTIME_STATE_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ggabf5068079e94310fb4b942df56ec1d10acc12ded1d9bd2a04d4b6346c186f8a67)、[FIDO2_RUNTIME_STATE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ggabf5068079e94310fb4b942df56ec1d10a8c7700d3df270e15fc9e6cd0a536bd9a)、[FIDO2_RUNTIME_STATE_WAITING_USER_PRESENCE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ggabf5068079e94310fb4b942df56ec1d10ac1dcd5cc47e59480df023bcc6d239909)、[FIDO2_RUNTIME_STATE_PROCESSING](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ggabf5068079e94310fb4b942df56ec1d10a64e677309cf5594b723f9b5c76e52774)。

FIDO2 子系统对外提供的运行时状态（Runtime States）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 20.3\_函数（Functions）

<a id="r_ga020303d5fcc00471feba64eec8e169c2"></a>

```c
int fido2_init (void)
```

相关声明：[fido2_init](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga020303d5fcc00471feba64eec8e169c2)。

初始化 FIDO2 子系统（Subsystem）。

<a id="r_gae7a1b8c0bf42ee2a0c3de0bc54c4fa72"></a>

```c
int fido2_start (void)
```

相关声明：[fido2_start](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae7a1b8c0bf42ee2a0c3de0bc54c4fa72)。

启动 FIDO2 认证器（Authenticator）。

<a id="r_gab41b4d957882b8d6844316ec2f3ccc95"></a>

```c
int fido2_stop (void)
```

相关声明：[fido2_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gab41b4d957882b8d6844316ec2f3ccc95)。

停止 FIDO2 认证器（Authenticator）。

<a id="r_gac2fecd9d7d18fbb8ff4b8e1083f86059"></a>

```c
int fido2_set_state_callback (fido2_state_callback_t cb, void *user_data)
```

相关声明：[fido2_set_state_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gac2fecd9d7d18fbb8ff4b8e1083f86059)、[fido2_state_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gad0a191f4a48998fe857dc6315d225d94)。

设置或清除唯一的 FIDO2 运行时状态回调（Runtime State Callback）。

<a id="r_gaeb4e348615069d77a81fb87c6970b640"></a>

```c
enum fido2_runtime_state fido2_get_state (void)
```

相关声明：[fido2_runtime_state](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gabf5068079e94310fb4b942df56ec1d10)、[fido2_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaeb4e348615069d77a81fb87c6970b640)。

获取 FIDO2 当前运行时状态（Runtime State）。

<a id="r_gaeb569aaa63c3c005d0df0b08c38896e1"></a>

```c
int fido2_reset (void)
```

相关声明：[fido2_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaeb569aaa63c3c005d0df0b08c38896e1)。

执行恢复出厂设置（Factory Reset）。


## 20.4\_原页交叉引用（Cross References）

- [zephyr/authentication/fido2/fido2_types.h](../api_source_reference/P262_fido2_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P258_fido2.h_源码浏览.md)
- [fido2_state_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gad0a191f4a48998fe857dc6315d225d94)
- [fido2_runtime_state](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gabf5068079e94310fb4b942df56ec1d10)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [FIDO2_RUNTIME_STATE_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ggabf5068079e94310fb4b942df56ec1d10acc12ded1d9bd2a04d4b6346c186f8a67)
- [FIDO2_RUNTIME_STATE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ggabf5068079e94310fb4b942df56ec1d10a8c7700d3df270e15fc9e6cd0a536bd9a)
- [FIDO2_RUNTIME_STATE_WAITING_USER_PRESENCE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ggabf5068079e94310fb4b942df56ec1d10ac1dcd5cc47e59480df023bcc6d239909)
- [FIDO2_RUNTIME_STATE_PROCESSING](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ggabf5068079e94310fb4b942df56ec1d10a64e677309cf5594b723f9b5c76e52774)
- [fido2_init](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga020303d5fcc00471feba64eec8e169c2)
- [fido2_start](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae7a1b8c0bf42ee2a0c3de0bc54c4fa72)
- [fido2_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gab41b4d957882b8d6844316ec2f3ccc95)
- [fido2_set_state_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gac2fecd9d7d18fbb8ff4b8e1083f86059)
- [fido2_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaeb4e348615069d77a81fb87c6970b640)
- [fido2_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaeb569aaa63c3c005d0df0b08c38896e1)

<a id="header-details"></a>

---

[上一章](P019_zephyr__xen__fdt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__bluetooth__classic__goep.h_文件参考.md)
