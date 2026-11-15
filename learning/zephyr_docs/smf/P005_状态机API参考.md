---
id: learning.zephyr-docs.smf.page-5
title: 状态机API参考
kind: reference
status: maintained
domains: [zephyr, smf, state-machine]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__smf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_状态机API参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__smf.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 5.1\_概述与数据结构

状态机框架API（State Machine Framework API）。原页给出的API版本（Version）为`0.2.0`。接口来自`<zephyr/smf.h>`。

```c
#include <zephyr/smf.h>
```

| 名称／声明 | 说明 |
| --- | --- |
| [smf_hooks](P009_状态机钩子.md) | 可选观测钩子（Instrumentation Hooks）的集合。 |
| [smf_state](P010_状态定义.md) | 可用于多个状态机的通用状态（General State）。 |
| [smf_ctx](P008_状态机上下文.md) | 定义状态机的当前上下文（Current Context）。 |

## 5.2\_宏（Macros）

<a id="ga5760b98a36ed1ac55eba700cf44c7e1e"></a>
<a id="r_ga5760b98a36ed1ac55eba700cf44c7e1e"></a>

### `SMF_CREATE_STATE`

```c
#define SMF_CREATE_STATE( _entry, _run, _exit, _parent, _initial )
```

创建带有初始转换（Initial Transitions）的层次状态（Hierarchical State）的宏。

展开值（Value）：

```c
{                                                                          \
        .entry   = _entry,                                                 \
        .run     = _run,                                                   \
        .exit    = _exit,                                                  \
        IF_ENABLED(CONFIG_SMF_ANCESTOR_SUPPORT, (.parent = _parent,))      \
        IF_ENABLED(CONFIG_SMF_INITIAL_TRANSITION, (.initial = _initial,))  \
}
```

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `_entry` | 状态进入函数（Entry Function），或`NULL`。 |
| `_run` | 状态运行函数（Run Function），或`NULL`。 |
| `_exit` | 状态退出函数（Exit Function），或`NULL`。 |
| `_parent` | 父状态对象（Parent State Object），或`NULL`。 |
| `_initial` | 初始转换目标状态对象（Initial Transition Object），或`NULL`。 |

<a id="ga0bccd3bf96e0887e8a610c1b06e22237"></a>
<a id="r_ga0bccd3bf96e0887e8a610c1b06e22237"></a>

### `SMF_CTX`

```c
#define SMF_CTX( o)
```

将用户定义对象转换为状态机上下文（State Machine Context）的宏。

展开值（Value）：

```c
((struct smf_ctx *)o)
```

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `o` | 指向用户定义对象（User-defined Object）的指针。 |

<a id="ga929c1e43e040ad15d7c87fb5a1029cb2"></a>
<a id="r_ga929c1e43e040ad15d7c87fb5a1029cb2"></a>

### `SMF_ERR_NULL_TRANSITION`

```c
#define SMF_ERR_NULL_TRANSITION 1
```

通过观测错误钩子（Instrumentation Error Hook）报告的错误码。

`smf_set_state`中的`new_state`为`NULL`。

<a id="gaadd57f63e4333e2e287bbb12bfadd18a"></a>
<a id="r_gaadd57f63e4333e2e287bbb12bfadd18a"></a>

### `SMF_ERR_TRANSITION_IN_EXIT`

```c
#define SMF_ERR_TRANSITION_IN_EXIT 2
```

在退出动作（Exit Action）中调用了`smf_set_state`。

## 5.3\_类型定义（Typedefs）

<a id="gab9de32d076908978a985e6ccdd7c388e"></a>
<a id="r_gab9de32d076908978a985e6ccdd7c388e"></a>

### `smf_action_hook`

```c
typedef void(* smf_action_hook) (struct smf_ctx *ctx, const struct smf_state *state, enum smf_action_type action_type)
```

在状态动作（进入／运行／退出，即Entry/Run/Exit）被调用之前执行。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `ctx` | 状态机上下文（State Machine Context）。 |
| `state` | 即将执行动作的状态。 |
| `action_type` | 动作类别：进入、运行或退出（Entry、Run、Exit）。 |

<a id="ga92c992228484976040d0c50bf82a31c3"></a>
<a id="r_ga92c992228484976040d0c50bf82a31c3"></a>

### `smf_error_hook`

```c
typedef void(* smf_error_hook) (struct smf_ctx *ctx, int error_code)
```

检测到无效操作（Invalid Operation）时调用。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `ctx` | 状态机上下文（State Machine Context）。 |
| `error_code` | `SMF_ERR_*`宏定义中的一个错误码。 |

<a id="gaff967f5e5edf9a2869355f4360b5f657"></a>
<a id="r_gaff967f5e5edf9a2869355f4360b5f657"></a>

### `smf_transition_hook`

```c
typedef void(* smf_transition_hook) (struct smf_ctx *ctx, const struct smf_state *source, const struct smf_state *dest)
```

在当前状态指针更新之后、新状态的进入动作执行之前调用。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `ctx` | 状态机上下文（State Machine Context）。 |
| `source` | 转换之前的状态（Previous State）。 |
| `dest` | 转换之后的新当前状态（New Current State）。 |

<a id="ga050cbb0a791dc062d222c0cfb4366f43"></a>
<a id="r_ga050cbb0a791dc062d222c0cfb4366f43"></a>

### `state_execution`

```c
typedef enum smf_state_result(* state_execution) (void *obj)
```

用于实现状态运行动作（Run Action）的函数指针。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `obj` | 指向用户定义对象的指针。 |

**返回值（Returns）**：是否应将事件传播给父状态。没有定义`CONFIG_SMF_ANCESTOR_SUPPORT`时忽略此返回值。

<a id="gace21c98a982b640c75951676d6ee3988"></a>
<a id="r_gace21c98a982b640c75951676d6ee3988"></a>

### `state_method`

```c
typedef void(* state_method) (void *obj)
```

用于实现状态进入动作和退出动作（Entry and Exit Actions）的函数指针。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `obj` | 指向用户定义对象的指针。 |

## 5.4\_枚举（Enumerations）

<a id="gad4a04d6058ae5323f7e93a3821d2f74f"></a>
<a id="r_gad4a04d6058ae5323f7e93a3821d2f74f"></a>

### `smf_action_type`

```c
enum smf_action_type
```

标识当前正在执行哪一类动作（Action Type）的枚举。

**枚举值（Enumerators）**

| 名称／声明 | 说明 |
| --- | --- |
| `SMF_ACTION_ENTRY` | 进入动作（Entry Action）。 |
| `SMF_ACTION_RUN` | 运行动作（Run Action）。 |
| `SMF_ACTION_EXIT` | 退出动作（Exit Action）。 |

**注意（Note）**：此枚举用于测试观测（Instrumentation）。

<a id="ga01e4e2d2f35a9ec790d5e3c5b9b91b55"></a>
<a id="r_ga01e4e2d2f35a9ec790d5e3c5b9b91b55"></a>

### `smf_state_result`

```c
enum smf_state_result
```

表示`state_execution`函数返回值的枚举（Enumeration）。

**枚举值（Enumerators）**

| 名称／声明 | 说明 |
| --- | --- |
| `SMF_EVENT_HANDLED` | —（原页未单列说明） |
| `SMF_EVENT_PROPAGATE` | —（原页未单列说明） |

## 5.5\_函数（Functions）

<a id="gae74fa0c5be2756cee5e1112a5c7b6da8"></a>
<a id="r_gae74fa0c5be2756cee5e1112a5c7b6da8"></a>

### `smf_get_current_executing_state()`

```c
static inline const struct smf_state * smf_get_current_executing_state ( const struct smf_ctx *const ctx)
```

获取当前正在执行的状态（Executing State）。

它可能是父状态（Parent State）。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `ctx` | 状态机上下文（State Machine Context）。 |

**返回值（Returns）**：当前正在执行的状态。

<a id="gabbb84eb59e5991b1ab51840f08a6a13f"></a>
<a id="r_gabbb84eb59e5991b1ab51840f08a6a13f"></a>

### `smf_get_current_leaf_state()`

```c
static inline const struct smf_state * smf_get_current_leaf_state ( const struct smf_ctx *const ctx)
```

获取当前叶状态（Leaf State）。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `ctx` | 状态机上下文（State Machine Context）。 |

**注意（Note）**：若HSM结构不正确，即初始转换没有正确配置，返回值可能是父状态（PARENT）。

**返回值（Returns）**：当前叶状态。

<a id="ga8399cfa9e793a7f188b4ed4fec9f4f90"></a>
<a id="r_ga8399cfa9e793a7f188b4ed4fec9f4f90"></a>

### `smf_run_state()`

```c
int32_t smf_run_state ( struct smf_ctx * ctx)
```

执行状态机的一次迭代（Iteration），包括相关父状态。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `ctx` | 状态机上下文（State Machine Context）。 |

**返回值（Returns）**：非零值表示应终止状态机。该值可能表示已经到达终止状态（Terminal State），或者检测到了需要终止状态机的错误。

<a id="ga4389086c6aa3167e8c49226323ae208d"></a>
<a id="r_ga4389086c6aa3167e8c49226323ae208d"></a>

### `smf_set_initial()`

```c
void smf_set_initial ( struct smf_ctx * ctx, const struct smf_state * init_state )
```

初始化状态机，并设置它的初始状态（Initial State）。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `ctx` | 状态机上下文（State Machine Context）。 |
| `init_state` | 状态机启动时进入的初始状态。 |

<a id="ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb"></a>
<a id="r_ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb"></a>

### `smf_set_state()`

```c
void smf_set_state ( struct smf_ctx * ctx, const struct smf_state * new_state )
```

改变状态机的状态。

此函数处理退出先前状态、进入目标状态的过程。对于层次状态机（HSM），不执行最近公共祖先（Least Common Ancestor）的进入和退出动作。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `ctx` | 状态机上下文（State Machine Context）。 |
| `new_state` | 要转换到的目标状态；原文说明`NULL`有效，并会退出所有状态。 |

> 译注：`new_state`的原文参数说明与同页`SMF_ERR_NULL_TRANSITION`、指南中的错误钩子说明存在矛盾。本次读取的[官方main实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/smf/smf.c)遇到`new_state == NULL`时，会记录错误、调用错误钩子并返回，不会退出所有状态。不要用此参数说明推导出可传空指针终止状态机；终止接口见`smf_set_terminate()`。可在[仓库参照实现](../../../lib/smf/smf.c)中跟踪相应分支，版本需分别核对。

<a id="gaae28c66f0652c99ba8e843eeaf02aaf7"></a>
<a id="r_gaae28c66f0652c99ba8e843eeaf02aaf7"></a>

### `smf_set_terminate()`

```c
void smf_set_terminate ( struct smf_ctx * ctx, int32_t val )
```

终止状态机。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `ctx` | 状态机上下文（State Machine Context）。 |
| `val` | 由`smf_run_state`函数返回的非零终止值（Termination Value）。 |

## 5.6\_观测钩子接口的源码补充译注

原API组页未列出条件编译接口`smf_set_hooks()`，但[指南](P001_状态机框架.md)和[源码浏览页](P007_状态机头文件源码.md)包含它。以下单独翻译本次读取的[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/smf.h)中的对应注释，避免与原API组页内容混淆；读取日期与摘要见[来源记录](../SOURCES.md)。

```c
void smf_set_hooks(struct smf_ctx *ctx, const struct smf_hooks *hooks);
```

在状态机上下文中设置观测钩子（Instrumentation Hooks）。必须在`smf_set_initial()`之后调用，因为初始化函数会将钩子指针重置为`NULL`；初始化期间执行的初始状态及其祖先的进入动作不会被捕获。

| 名称／声明 | 说明 |
| --- | --- |
| `ctx` | 状态机上下文。 |
| `hooks` | 指向钩子结构体的指针；传`NULL`可禁用钩子。所指向结构体的生命周期必须长于状态机。 |

此声明位于`CONFIG_SMF_INSTRUMENTATION`条件编译区内。官方自动生成参考没有展示此接口，不表示源码中不存在它。

<a id="nested-classes"></a>
<a id="define-members"></a>
<a id="typedef-members"></a>
<a id="enum-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="ggad4a04d6058ae5323f7e93a3821d2f74fa9f811fe99a13371b4ecf6a5f76567869"></a>
<a id="ggad4a04d6058ae5323f7e93a3821d2f74fa22829dab2469999645833b3b2fbb5350"></a>
<a id="ggad4a04d6058ae5323f7e93a3821d2f74fa7c7e8f8ed2883320dc48b34c783f2100"></a>
<a id="gga01e4e2d2f35a9ec790d5e3c5b9b91b55a088a71df8c1eb56aec8e4ef647a2248a"></a>
<a id="gga01e4e2d2f35a9ec790d5e3c5b9b91b55af86126b6ae29cfa0c1816bc5fb2873b6"></a>
<a id="doc-func-members"></a>
<a id="r_smf_5Fhooks"></a>
<a id="r_smf_5Fstate"></a>
<a id="r_smf_5Fctx"></a>
<a id="header-nested-classes"></a>
<a id="header-define-members"></a>
<a id="header-typedef-members"></a>
<a id="header-enum-members"></a>
<a id="header-func-members"></a>
<a id="header-details"></a>
<a id="header-doc-define-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="header-doc-enum-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P004_状态机计算器.md) · [返回大纲](大纲.md) · [下一章](P006_状态机头文件参考.md)
