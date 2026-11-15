---
id: learning.zephyr-docs.api-protocol-topic-reference.page-23
title: 轻量级M2M（LwM2M）的路径辅助宏。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__path__helpers.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_轻量级M2M（LwM2M）的路径辅助宏。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__path__helpers.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

自 Zephyr 2.5 起提供；API 版本为 0.8.0。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 23.1\_宏定义（Macros）

<a id="r_ga0ac92ffa4a22bcd407a19e768a5720bd"></a>

```c
#define LWM2M_PATH(...)
```

相关声明：[LWM2M_PATH](#ga0ac92ffa4a22bcd407a19e768a5720bd)。

使用数值分量（Numeric Components）生成轻量级机器到机器协议字符串路径（LwM2M String Paths）。

<a id="r_gac3c46145eae19f8c8608429e5b4e9250"></a>

```c
#define LWM2M_OBJ(...)
```

相关声明：[LWM2M_OBJ](#gac3c46145eae19f8c8608429e5b4e9250)。

初始化 LwM2M 对象结构体（Object Structure）。

## 23.2\_详细说明（Detailed Documentation）

<a id="gac3c46145eae19f8c8608429e5b4e9250"></a>

### `LWM2M_OBJ`

```c
#define LWM2M_OBJ ( ...)
```

```c
#include <zephyr/net/lwm2m_path.h>
```

展开值（Value）：

```c
GET_OBJ_MACRO(__VA_ARGS__, LWM2M_OBJ4, LWM2M_OBJ3, LWM2M_OBJ2, LWM2M_OBJ1)(__VA_ARGS__)
```

初始化 LwM2M 对象结构体（Object Structure）。

接受至少一个、至多四个参数。填充 `lwm2m_obj_path` 结构体并设置层级（level）。

例如：

原始示例（Example）：

```c
struct lwm2m_obj_path p = LWM2M_OBJ(MY_OBJ, 0, RESOURCE);
```

也可在函数实参位置使用，返回从栈（stack）上分配的结构体。

原始示例（Example）：

```c
lwm2m_notify_observer_path(&LWM2M_OBJ(MY_OBJ, inst_id, RESOURCE));
```

<a id="ga0ac92ffa4a22bcd407a19e768a5720bd"></a>

### `LWM2M_PATH`

```c
#define LWM2M_PATH ( ...)
```

```c
#include <zephyr/net/lwm2m_path.h>
```

展开值（Value）：

```c
LWM2M_PATH_MACRO(__VA_ARGS__, LWM2M_PATH4, LWM2M_PATH3, \
                 LWM2M_PATH2, LWM2M_PATH1)(__VA_ARGS__)
```

使用数值分量（Numeric Components）生成轻量级机器到机器协议字符串路径（LwM2M String Paths）。

接受至少一个、至多四个参数。预处理器（preprocessor）会将每个参数字符串化（stringify），因此使用非字面量（non-literals）调用时，很可能无法获得预期结果。

例如：

原始示例（Example）：

```c
#define MY_OBJ_ID 3
LWM2M_PATH(MY_OBJ_ID, 0, 1)
```

会求值得到 `"3/0/1"`，而下一个示例

原始示例（Example）：

```c
int x = 3;
LWM2M_PATH(x, 0, 1)
```

求值得到 `"x/0/1"`。


## 23.3\_原页交叉引用（Cross References）

- [zephyr/net/lwm2m_path.h](../api_file_configuration_reference/P046_zephyr__net__lwm2m_path.h_文件参考.md)
- [lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__lwm2m__path__helpers_html_gac3c46145eae19f8c8608429e5b4e9250"></a>
<a id="astructlwm2m__obj__path_html"></a>
<a id="agroup__lwm2m__path__helpers_html_ga0ac92ffa4a22bcd407a19e768a5720bd"></a>

---

[上一章](P022_L2CAP 通道标识符（L2CAP channel identifiers）.md) · [返回大纲](大纲.md) · [下一章](P024_向量按位与（Vector bitwise AND）.md)
