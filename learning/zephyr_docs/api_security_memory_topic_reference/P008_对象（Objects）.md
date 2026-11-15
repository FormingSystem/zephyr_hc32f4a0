---
id: learning.zephyr-docs.api-security-memory-topic-reference.page-8
title: 对象（Objects）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_对象（Objects）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

为每一种类型提供身份和属性的公共基类。

<a id="details"></a>

为所有类型提供身份和属性的公共基类（Common Base）。每个元素（Element）和焊盘（Pad）都将 Objects 嵌入为首成员，因此向上转换（Upcasting）只需普通 C 类型转换。基类保存框架管理对象所需的信息：标识（ID）、指向所属容器的指针、供容器将子对象放入同一列表的节点，以及遍历器用于决定能否向下进入的标志字段。

它还保存属性回调（Property Callbacks）。属性（Property）让调用者无需知道元素的具体类型，就能配置文件路径、设备或队列深度等内容；应通过 `mpipe_object_set_properties` 和 `mpipe_object_get_properties` 访问，而不是直接调用回调。属性不同于能力（Capability）：属性只配置一个元素，无需其他对象同意；能力描述穿过链路的数据，数据流动前链路两端必须达成一致。参见能力结构（Capability Structure）。

<a id="header-files"></a>
<a id="files"></a>

## 8.1\_文件（Files）

<a id="r_mpipe_5Fobject_2Eh"></a>

```c
file mpipe_object.h
```

相关声明：[mpipe_object.h](../api_file_management_reference/P037_zephyr__mpipe__mpipe_object.h_文件参考.md)。

对象（Object）：每个mpipe类型都嵌入的基类。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.2\_数据结构（Data Structures）

<a id="r_mpipe_5Fobject"></a>

```c
struct mpipe_object
```

相关声明：[mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)。

基础对象结构（Base Object Structure）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.3\_宏定义（Macros）

<a id="r_ga40d41093fdd92de417133e57476d6e24"></a>

```c
#define MPIPE_OBJECT_FLAG_BASE BIT(0)
```

相关声明：[MPIPE_OBJECT_FLAG_BASE](#ga40d41093fdd92de417133e57476d6e24)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

对象的基础标志（base flag）。

<a id="r_ga1b65711b9e9f2e53f4a85d9db490cc91"></a>

```c
#define MPIPE_OBJECT_FLAG_BIN BIT(1)
```

相关声明：[MPIPE_OBJECT_FLAG_BIN](#ga1b65711b9e9f2e53f4a85d9db490cc91)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

该对象为容器（Bins），拥有自己的子对象。

<a id="r_gaecb3a88ad49c27402eebe277c73bc825"></a>

```c
#define MPIPE_PROP_LIST_END UINT32_MAX
```

相关声明：[MPIPE_PROP_LIST_END](#gaecb3a88ad49c27402eebe277c73bc825)、[UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)。

标记属性列表结束的哨兵值（sentinel value）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.4\_函数（Functions）

<a id="r_gaa248dc28bf93b5426a9614e8611f60fe"></a>

```c
void mpipe_object_init (struct mpipe_object *obj)
```

相关声明：[mpipe_object_init](#gaa248dc28bf93b5426a9614e8611f60fe)、[mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)。

将 `mpipe_object` 的所有字段初始化为零。

<a id="r_gae63735281ccac01779ba1e037e438641"></a>

```c
int mpipe_object_set_properties (struct mpipe_object *obj,...)
```

相关声明：[mpipe_object_set_properties](#gae63735281ccac01779ba1e037e438641)、[mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)。

设置 `mpipe_object` 的多个属性（properties）。

<a id="r_ga7ae53fbbd40a3886b0baf767d1e5c4c5"></a>

```c
int mpipe_object_get_properties (struct mpipe_object *obj,...)
```

相关声明：[mpipe_object_get_properties](#ga7ae53fbbd40a3886b0baf767d1e5c4c5)、[mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)。

获取 `mpipe_object` 的多个属性值。

## 8.5\_详细说明（Detailed Documentation）

<a id="ga40d41093fdd92de417133e57476d6e24"></a>

### `MPIPE_OBJECT_FLAG_BASE`

```c
#define MPIPE_OBJECT_FLAG_BASE BIT(0)
```

```c
#include <zephyr/mpipe/mpipe_object.h>
```

对象的基础标志（base flag）。

<a id="ga1b65711b9e9f2e53f4a85d9db490cc91"></a>

### `MPIPE_OBJECT_FLAG_BIN`

```c
#define MPIPE_OBJECT_FLAG_BIN BIT(1)
```

```c
#include <zephyr/mpipe/mpipe_object.h>
```

该对象为容器（Bins），拥有自己的子对象。

由 `mpipe_bin_init()` 设置，告知遍历器（Walker）可以向下进入该元素。

<a id="gaecb3a88ad49c27402eebe277c73bc825"></a>

### `MPIPE_PROP_LIST_END`

```c
#define MPIPE_PROP_LIST_END UINT32_MAX
```

```c
#include <zephyr/mpipe/mpipe_object.h>
```

标记属性列表结束的哨兵值（sentinel value）。

<a id="ga7ae53fbbd40a3886b0baf767d1e5c4c5"></a>

### `mpipe_object_get_properties()`

```c
int mpipe_object_get_properties ( struct mpipe_object * obj, ... )
```

```c
#include <zephyr/mpipe/mpipe_object.h>
```

获取 `mpipe_object` 的多个属性值。

获取指定对象的一个或多个属性值（Property Values）。参数必须按 `{key, value}` 对依次提供，并以 `MPIPE_PROP_LIST_END` 终止。

使用示例：

原始示例（Example）：

```c
const char *path;

mpipe_object_get_properties(&file_src.src.element.object,
                            MY_PROP_PATH, &path,
                            MPIPE_PROP_LIST_END);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `obj` | 指向 Objects 的指针。 |
| `...` | 可变长度的 `{uint32_t key, void *val}` 参数对列表，以 `MPIPE_PROP_LIST_END` 终止。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 对象未提供属性读取函数（Property Getter）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，否则返回第一个失败读取函数（Getter）的错误，余下参数对不再读取。

<a id="gaa248dc28bf93b5426a9614e8611f60fe"></a>

### `mpipe_object_init()`

```c
void mpipe_object_init ( struct mpipe_object * obj)
```

```c
#include <zephyr/mpipe/mpipe_object.h>
```

将 `mpipe_object` 的所有字段初始化为零。

初始化任何嵌入 `mpipe_object` 的结构体时，必须首先调用本函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `obj` | 指向待初始化的 `mpipe_object` 的指针。 |

<a id="gae63735281ccac01779ba1e037e438641"></a>

### `mpipe_object_set_properties()`

```c
int mpipe_object_set_properties ( struct mpipe_object * obj, ... )
```

```c
#include <zephyr/mpipe/mpipe_object.h>
```

设置 `mpipe_object` 的多个属性（properties）。

设置指定对象的一个或多个属性（Properties）。参数必须按 `{key, value}` 对依次提供，并以 `MPIPE_PROP_LIST_END` 终止。

使用示例：

原始示例（Example）：

```c
mpipe_object_set_properties(&file_src.src.element.object,
                            MY_PROP_PATH, "/SD:/in.bin",
                            MPIPE_PROP_LIST_END);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `obj` | 指向 Objects 的指针。 |
| `...` | 可变长度的 `{uint32_t key, const void *val}` 参数对列表；键取自元素的属性枚举（Property Enumeration），以 `MPIPE_PROP_LIST_END` 终止。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 对象未提供属性设置函数（Property Setter）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，否则返回第一个失败设置函数（Setter）的错误，余下参数对不再应用。


## 8.6\_原页交叉引用（Cross References）

- [mpipe_object.h](../api_file_management_reference/P037_zephyr__mpipe__mpipe_object.h_文件参考.md)
- [mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [容器（Bins）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html)
- [UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)
- [对象（Objects）](P008_对象（Objects）.md)
- [能力结构（Capability Structure）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html)
- [mpipe_bin_init()](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html#gab9a27c7642bd57189aa1f62da3c080e3)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="agroup__mpipe__object_html_ga7ae53fbbd40a3886b0baf767d1e5c4c5"></a>
<a id="agroup__mpipe__object_html_gaecb3a88ad49c27402eebe277c73bc825"></a>
<a id="agroup__mpipe__object_html_gae63735281ccac01779ba1e037e438641"></a>

---

[上一章](P007_存储器控制器（MEMC）.md) · [返回大纲](大纲.md) · [下一章](P009_源（Sources）.md)
