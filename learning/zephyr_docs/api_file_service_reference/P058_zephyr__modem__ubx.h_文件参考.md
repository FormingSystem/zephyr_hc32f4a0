---
id: learning.zephyr-docs.api-file-service-reference.page-58
title: zephyr__modem__ubx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ubx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_zephyr\_\_modem\_\_ubx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ubx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/modem/pipe.h>
#include <zephyr/modem/ubx/protocol.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 58.1\_数据结构（Data Structures）

<a id="r_modem_5Fubx_5Fmatch"></a>

```c
struct modem_ubx_match
```

相关声明：[modem_ubx_match](../modem_wireless_model_reference/P063_modem_ubx_match_结构体.md)。

<a id="r_modem_5Fubx_5Fscript"></a>

```c
struct modem_ubx_script
```

相关声明：[modem_ubx_script](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md)。

<a id="r_modem_5Fubx"></a>

```c
struct modem_ubx
```

相关声明：[modem_ubx](../modem_wireless_model_reference/P061_modem_ubx_结构体.md)。

<a id="r_modem_5Fubx_5Fconfig"></a>

```c
struct modem_ubx_config
```

相关声明：[modem_ubx_config](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 58.2\_宏定义（Macros）

<a id="r_ga8a37614e3a9cf6d4773b9e74de79d340"></a>

```c
#define MODEM_UBX_MATCH_ARRAY_DEFINE(_name, ...)
```

相关声明：[MODEM_UBX_MATCH_ARRAY_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#ga8a37614e3a9cf6d4773b9e74de79d340)。

<a id="r_ga4c04f643a1ea9f0fc940d286713be30e"></a>

```c
#define MODEM_UBX_MATCH_DEFINE(_class_id, _msg_id, _handler)
```

相关声明：[MODEM_UBX_MATCH_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#ga4c04f643a1ea9f0fc940d286713be30e)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 58.3\_类型定义（Typedefs）

<a id="r_gae0bfe22e7e8d7d38ae9f41648f7fcfda"></a>

```c
typedef void(* modem_ubx_match_callback) (struct modem_ubx *ubx, const struct ubx_frame *frame, size_t len, void *user_data)
```

相关声明：[modem_ubx_match_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#gae0bfe22e7e8d7d38ae9f41648f7fcfda)、[modem_ubx](../modem_wireless_model_reference/P061_modem_ubx_结构体.md)、[ubx_frame](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 58.4\_函数（Functions）

<a id="r_ga4e459f955e34c9059702c3d7f9794948"></a>

```c
int modem_ubx_attach (struct modem_ubx *ubx, struct modem_pipe *pipe)
```

相关声明：[modem_ubx_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#ga4e459f955e34c9059702c3d7f9794948)、[modem_ubx](../modem_wireless_model_reference/P061_modem_ubx_结构体.md)。

将管道（Pipe）连接到 Modem Ubx。

<a id="r_ga68210f4afd5880c532d82fd0bac1d933"></a>

```c
void modem_ubx_release (struct modem_ubx *ubx)
```

相关声明：[modem_ubx_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#ga68210f4afd5880c532d82fd0bac1d933)、[modem_ubx](../modem_wireless_model_reference/P061_modem_ubx_结构体.md)。

从 Modem Ubx 实例（Instance）释放管道（Pipe）。

<a id="r_gaf49363fb4decb4656566b508a061212f"></a>

```c
int modem_ubx_init (struct modem_ubx *ubx, const struct modem_ubx_config *config)
```

相关声明：[modem_ubx_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#gaf49363fb4decb4656566b508a061212f)、[modem_ubx](../modem_wireless_model_reference/P061_modem_ubx_结构体.md)、[modem_ubx_config](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md)。

初始化 Modem Ubx 实例（Instance）。

<a id="r_ga770650b055fd597f000a1d4f9daaf712"></a>

```c
int modem_ubx_run_script (struct modem_ubx *ubx, struct modem_ubx_script *script)
```

相关声明：[modem_ubx_run_script](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#ga770650b055fd597f000a1d4f9daaf712)、[modem_ubx](../modem_wireless_model_reference/P061_modem_ubx_结构体.md)、[modem_ubx_script](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md)。

写入 `script.request` 中的 UBX 帧（UBX Frame），并在有响应时读回其响应（Response）。

<a id="r_ga0fd0def90f6304e679c4123e3c8d0c3f"></a>

```c
int modem_ubx_run_script_for_each (struct modem_ubx *ubx, struct modem_ubx_script *script, struct ubx_frame *array, size_t array_size)
```

相关声明：[modem_ubx_run_script_for_each](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#ga0fd0def90f6304e679c4123e3c8d0c3f)、[modem_ubx](../modem_wireless_model_reference/P061_modem_ubx_结构体.md)、[modem_ubx_script](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md)、[ubx_frame](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md)。


## 58.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/modem/pipe.h](../api_source_supplement_reference/P145_pipe.h_源码浏览.md)
- [zephyr/modem/ubx/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P883_ubx.h_源码浏览.md)
- [modem_ubx_match](../modem_wireless_model_reference/P063_modem_ubx_match_结构体.md)
- [modem_ubx_script](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md)
- [modem_ubx](../modem_wireless_model_reference/P061_modem_ubx_结构体.md)
- [modem_ubx_config](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md)
- [MODEM_UBX_MATCH_ARRAY_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#ga8a37614e3a9cf6d4773b9e74de79d340)
- [MODEM_UBX_MATCH_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#ga4c04f643a1ea9f0fc940d286713be30e)
- [modem_ubx_match_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#gae0bfe22e7e8d7d38ae9f41648f7fcfda)
- [ubx_frame](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md)
- [modem_ubx_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#ga4e459f955e34c9059702c3d7f9794948)
- [modem_ubx_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#ga68210f4afd5880c532d82fd0bac1d933)
- [modem_ubx_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#gaf49363fb4decb4656566b508a061212f)
- [modem_ubx_run_script](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#ga770650b055fd597f000a1d4f9daaf712)
- [modem_ubx_run_script_for_each](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#ga0fd0def90f6304e679c4123e3c8d0c3f)

---

[上一章](P057_zephyr__drivers__clock_control__tisci_clock_control.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P059_zephyr__usb__class__usbd_uac2.h_文件参考.md)
