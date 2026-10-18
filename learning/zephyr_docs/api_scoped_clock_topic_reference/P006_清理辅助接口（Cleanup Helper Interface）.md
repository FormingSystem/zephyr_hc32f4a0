---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-6
title: 清理辅助接口（Cleanup Helper Interface）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_清理辅助接口（Cleanup Helper Interface）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="r_ga4faf2c585a3fa2ce28480a5e2805ca8b"></a>

```c
#define SCOPE_VAR_DEFINE(_name, _type, _exit_fn, _init_fn, ...)
```

相关声明：[SCOPE_VAR_DEFINE](#ga4faf2c585a3fa2ce28480a5e2805ca8b)。

定义作用域变量类型（Scoped Variable Type）。

<a id="r_gab584b9adf45e13376c0f8e0b817a6213"></a>

```c
#define SCOPE_GUARD_DEFINE(_name, _type, _lock, _unlock)
```

相关声明：[SCOPE_GUARD_DEFINE](#gab584b9adf45e13376c0f8e0b817a6213)。

定义作用域守卫类型（Scoped Guard Type）。

<a id="r_ga88752a55762b11e721c3052c6adc401a"></a>

```c
#define SCOPE_COND_GUARD_DEFINE(_name, _type, _try_lock, _unlock)
```

相关声明：[SCOPE_COND_GUARD_DEFINE](#ga88752a55762b11e721c3052c6adc401a)。

定义条件式、可失败的作用域守卫类型（Conditional/Failable Scoped Guard Type）。

<a id="r_ga07847cc6bb3cd5f63b4d05e084eb9203"></a>

```c
#define SCOPE_DEFER_DEFINE(_func, ...)
```

相关声明：[SCOPE_DEFER_DEFINE](#ga07847cc6bb3cd5f63b4d05e084eb9203)。

定义作用域延后执行类型（Scoped Defer Type）。

<a id="r_ga62362f13860dbea4361e7cf149801d3f"></a>

```c
#define scope_var(_name, _var)
```

相关声明：[scope_var](#ga62362f13860dbea4361e7cf149801d3f)。

声明具有自动清理（Automatic Cleanup）功能的变量。

<a id="r_ga096c421f2ba9d7acd68039d493a80b63"></a>

```c
#define scope_var_init(_name, _var, _init_expr)
```

相关声明：[scope_var_init](#ga096c421f2ba9d7acd68039d493a80b63)。

通过直接初始化（Direct Initialization）声明具有自动清理（Automatic Cleanup）功能的变量。

<a id="r_ga3905160905199178d29b66084f237f4e"></a>

```c
#define scope_guard(_name)
```

相关声明：[scope_guard](#ga3905160905199178d29b66084f237f4e)。

获取作用域守卫锁（Scoped Guard Lock）。

<a id="r_gad7807c92614173dacfe7af2ca6a572ab"></a>

```c
#define scoped_guard(_name, ...)
```

相关声明：[scoped_guard](#gad7807c92614173dacfe7af2ca6a572ab)。

为随后代码块的生命周期（Lifetime）获取守卫（Guard）。

<a id="r_ga1f5c0f74610d1bbcc1fd3c7914ab9a7c"></a>

```c
#define scoped_cond_guard(_name, _fail, ...)
```

相关声明：[scoped_cond_guard](#ga1f5c0f74610d1bbcc1fd3c7914ab9a7c)。

为随后代码块的生命周期（Lifetime）有条件地获取守卫（Guard）。

<a id="r_ga5ea0ef9eed956fa112b069d87f8b05e5"></a>

```c
#define scope_defer(_name)
```

相关声明：[scope_defer](#ga5ea0ef9eed956fa112b069d87f8b05e5)。

注册作用域延后调用（Scoped Deferred Call）。

## 6.2\_详细说明（Detailed Documentation）

<a id="ga88752a55762b11e721c3052c6adc401a"></a>

### `SCOPE_COND_GUARD_DEFINE`

```c
#define SCOPE_COND_GUARD_DEFINE ( _name, _type, _try_lock, _unlock )
```

```c
#include <zephyr/cleanup.h>
```

展开值（Value）：

```c
SCOPE_VAR_DEFINE(guard_##_name, _type, if (_T != NULL) { _unlock; },                       \
                 ((_try_lock) ? _T : NULL), _type _T)
```

定义条件式、可失败的作用域守卫类型（Conditional/Failable Scoped Guard Type）。

此宏定义锁获取可能失败的守卫（Guard），供 scoped_cond_guard 使用。与 SCOPE_GUARD_DEFINE 不同，它会判断 acquire 表达式是否成功：结果为真时，守卫保存类型为 _type 的 _T，并在退出作用域（Scope Exit）时执行 release 表达式；结果为假时，守卫保存 NULL，不释放任何内容。

用法（Usage）：

原始示例（Example）：

```c
SCOPE_COND_GUARD_DEFINE(k_mutex_try, struct k_mutex *,
                        k_mutex_lock(_T, K_NO_WAIT) == 0,
                        (void)k_mutex_unlock(_T));
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 守卫名称（Guard Name），将添加 guard_ 前缀。 |
| `_type` | 锁对象类型（Lock Object Type），必须是指针类型。 |
| `_try_lock` | 获取锁时求值为真的表达式（Expression），可以引用 _T。 |
| `_unlock` | 释放锁的表达式（Expression），可以引用 _T。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_SCOPE_CLEANUP_HELPERS 时可用。

<a id="ga5ea0ef9eed956fa112b069d87f8b05e5"></a>

### `scope_defer`

```c
#define scope_defer ( _name)
```

```c
#include <zephyr/cleanup.h>
```

展开值（Value）：

```c
scope_var(defer_##_name, Z_UNIQUE_ID(defer))
```

注册作用域延后调用（Scoped Deferred Call）。

此宏创建一个延后清理变量（Defer Variable），名称由系统自动生成且唯一。离开作用域（Scope）时，defer 会执行其清理动作（Cleanup Action）。

用法（Usage）：

原始示例（Example）：

```c
scope_defer(k_mutex_unlock)(&my_mutex);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 延后清理类型名称（Defer Type Name），由 SCOPE_DEFER_DEFINE 定义，或由 SCOPE_VAR_DEFINE 使用 defer_ 前缀定义。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_SCOPE_CLEANUP_HELPERS 时可用。

<a id="ga07847cc6bb3cd5f63b4d05e084eb9203"></a>

### `SCOPE_DEFER_DEFINE`

```c
#define SCOPE_DEFER_DEFINE ( _func, ... )
```

```c
#include <zephyr/cleanup.h>
```

展开值（Value）：

```c
COND_CODE_0(NUM_VA_ARGS(__VA_ARGS__),                                                      \
            (Z_SCOPE_DEFER_DEFINE_VOID(_func)),                                            \
            (Z_SCOPE_DEFER_DEFINE_N(_func, __VA_ARGS__)))
```

定义作用域延后执行类型（Scoped Defer Type）。

此宏定义一种延后清理（Defer），在变量离开作用域（Scope）时执行清理函数（Cleanup Function）。与守卫（Guards）不同，defer 不在初始化时获取资源。

用法（Usage）：

原始示例（Example）：

```c
SCOPE_DEFER_DEFINE(k_free, void *);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_func` | 清理时要调用的函数（Cleanup Function）。 |
| `...` | 传给清理函数的参数类型（Argument Types）。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_SCOPE_CLEANUP_HELPERS 时可用。

<a id="ga3905160905199178d29b66084f237f4e"></a>

### `scope_guard`

```c
#define scope_guard ( _name)
```

```c
#include <zephyr/cleanup.h>
```

展开值（Value）：

```c
scope_var(guard_##_name, Z_UNIQUE_ID(guard))
```

获取作用域守卫锁（Scoped Guard Lock）。

此宏创建一个守卫变量（Guard Variable），名称由系统自动生成且唯一。守卫在初始化时获取锁，并在离开作用域（Scope）时释放锁。

用法（Usage）：

原始示例（Example）：

```c
scope_guard(k_mutex)(&my_mutex);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 守卫类型名称（Guard Type Name），由 SCOPE_GUARD_DEFINE 定义，或由 SCOPE_VAR_DEFINE 使用 guard_ 前缀定义。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_SCOPE_CLEANUP_HELPERS 时可用。

<a id="gab584b9adf45e13376c0f8e0b817a6213"></a>

### `SCOPE_GUARD_DEFINE`

```c
#define SCOPE_GUARD_DEFINE ( _name, _type, _lock, _unlock )
```

```c
#include <zephyr/cleanup.h>
```

展开值（Value）：

```c
SCOPE_VAR_DEFINE(                                                                          \
        guard_##_name, _type, if (_T != NULL) { _unlock; }, ({                             \
                _lock;                                                                     \
                _T;                                                                        \
        }),                                                                                \
        _type _T)
```

定义作用域守卫类型（Scoped Guard Type）。

此宏定义一种守卫（Guard），在初始化时自动获取锁，并在离开作用域（Scope）时释放锁。

用法（Usage）：

原始示例（Example）：

```c
SCOPE_GUARD_DEFINE(k_mutex, struct k_mutex *,
                   (void)k_mutex_lock(_T, K_FOREVER),
                   (void)k_mutex_unlock(_T));
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 守卫名称（Guard Name），将添加 guard_ 前缀。 |
| `_type` | 锁对象类型（Lock Object Type），通常为指针。 |
| `_lock` | 获取锁的表达式（Expression），可以引用 _T。 |
| `_unlock` | 释放锁的表达式（Expression），可以引用 _T。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_SCOPE_CLEANUP_HELPERS 时可用。

<a id="ga62362f13860dbea4361e7cf149801d3f"></a>

### `scope_var`

```c
#define scope_var ( _name, _var )
```

```c
#include <zephyr/cleanup.h>
```

展开值（Value）：

```c
cleanup_##_name##_t _var __cleanup(cleanup_##_name##_exit) = cleanup_##_name##_init
```

声明具有自动清理（Automatic Cleanup）功能的变量。

此宏使用先前定义的清理辅助类型（Cleanup Helper），声明一个带自动清理（Automatic Cleanup）的变量。离开作用域（Scope）时会自动清理该变量。

变量通过调用 SCOPE_VAR_DEFINE 定义的 init 函数初始化。如果希望使用直接表达式初始化变量，而不调用 init 函数，请使用 scope_var_init。

用法（Usage）：

原始示例（Example）：

```c
scope_var(some_type, my_var)(init_args);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 清理辅助类型名称（Cleanup Helper Name），由 SCOPE_VAR_DEFINE 定义。 |
| `_var` | 要声明的变量名称（Variable Name）。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_SCOPE_CLEANUP_HELPERS 时可用。

**参阅（See Also）**：另请参见（See Also）：scope_var_init，可直接初始化而不调用 init 函数。

<a id="ga4faf2c585a3fa2ce28480a5e2805ca8b"></a>

### `SCOPE_VAR_DEFINE`

```c
#define SCOPE_VAR_DEFINE ( _name, _type, _exit_fn, _init_fn, ... )
```

```c
#include <zephyr/cleanup.h>
```

展开值（Value）：

```c
static inline void __maybe_unused cleanup_##_name##_exit(_type *p)                         \
{                                                                                          \
        _type _T = *p;                                                                     \
        _exit_fn;                                                                          \
}                                                                                          \
static inline _type __maybe_unused cleanup_##_name##_init(__VA_ARGS__)                     \
{                                                                                          \
        _type t = _init_fn;                                                                \
        return t;                                                                          \
}                                                                                          \
typedef _type cleanup_##_name##_t
```

定义作用域变量类型（Scoped Variable Type）。

此宏定义新的清理辅助类型（Cleanup Helper），可与 __cleanup 属性一起使用，在变量离开作用域（Scope）时自动执行清理代码（Cleanup Code）。

此宏创建以下内容：

- 一个退出函数（Exit Function）`cleanup_<name>_exit`，执行清理代码。
- 一个初始化函数（Init Function）`cleanup_<name>_init`，初始化变量。
- 一个用于该类型的类型别名（Typedef）`cleanup_<name>_t`。

用法（Usage）：

原始示例（Example）：

```c
struct foo {
    int value;
};

static inline struct foo *foo_constructor(int value)
{
    struct foo *ptr = k_malloc(sizeof(struct foo));

    if (ptr != NULL) {
        ptr->value = value;
    }

    return ptr;
}

static inline void foo_destructor(struct foo *ptr)
{
    k_free(ptr);
}

// Define the cleanup helper
SCOPE_VAR_DEFINE(foo, struct foo *, foo_destructor(_T), foo_constructor(val), int val);

static int some_function(void)
{
    // The scope_var macro declares 'f' with automatic cleanup
    scope_var(foo, f)(42);
    if (f == NULL) {
        return -ENOMEM;
    }

    // Use f normally - it points to an allocated and initialized struct foo
    printk("Value: %d\n", f->value);

    // No need to manually free - foo_destructor is called automatically
    // when 'f' goes out of scope
}
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 清理辅助类型名称（Cleanup Helper Name）。 |
| `_type` | 待清理变量的类型（Variable Type）。 |
| `_exit_fn` | 变量离开作用域（Scope）时执行的清理代码（Cleanup Code），可以引用 _T。 |
| `_init_fn` | 变量初始化表达式（Initialization Expression）。 |
| `...` | 初始化参数（Initialization Arguments），为可变参数。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_SCOPE_CLEANUP_HELPERS 时可用。

<a id="ga096c421f2ba9d7acd68039d493a80b63"></a>

### `scope_var_init`

```c
#define scope_var_init ( _name, _var, _init_expr )
```

```c
#include <zephyr/cleanup.h>
```

展开值（Value）：

```c
cleanup_##_name##_t _var __cleanup(cleanup_##_name##_exit) = (_init_expr)
```

通过直接初始化（Direct Initialization）声明具有自动清理（Automatic Cleanup）功能的变量。

此宏使用先前定义的清理辅助类型（Cleanup Helper），声明一个带自动清理（Automatic Cleanup）的变量。离开作用域（Scope）时会自动清理该变量。

与 scope_var 不同，此宏接受直接初始化表达式（Direct Initialization Expression），而不调用 SCOPE_VAR_DEFINE 定义的 init 函数。需要绕过 init 函数直接初始化变量时使用，例如使用结构体初始化器、其他函数或字面值。

用法（Usage）：

原始示例（Example）：

```c
scope_var_init(some_type, my_var, {0});
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 清理辅助类型名称（Cleanup Helper Name），由 SCOPE_VAR_DEFINE 定义。 |
| `_var` | 要声明的变量名称（Variable Name）。 |
| `_init_expr` | 变量的直接初始化表达式（Direct Initialization Expression），例如 {0}、NULL 或函数调用。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_SCOPE_CLEANUP_HELPERS 时可用。

**参阅（See Also）**：另请参见（See Also）：scope_var，通过 init 函数初始化。

<a id="ga1f5c0f74610d1bbcc1fd3c7914ab9a7c"></a>

### `scoped_cond_guard`

```c
#define scoped_cond_guard ( _name, _fail, ... )
```

```c
#include <zephyr/cleanup.h>
```

展开值（Value）：

```c
Z_SCOPED_COND_GUARD(_name, Z_UNIQUE_ID(scoped_g), Z_UNIQUE_ID(scoped_done), _fail,         \
                    __VA_ARGS__)
```

为随后代码块的生命周期（Lifetime）有条件地获取守卫（Guard）。

此宏尝试获取一个带条件、可能失败的作用域守卫（Conditional Scoped Guard）；成功时，在紧随其后的花括号代码块期间持有锁，离开该代码块时立即释放。无法获取锁时，执行 _fail 并跳过代码块。

成功时，代码块恰好执行一次。以任何方式离开代码块都会释放锁，包括 break、return 和 goto；continue 的行为与 break 相同。

用法（Usage）：

原始示例（Example）：

```c
scoped_cond_guard(k_mutex_try, return -EBUSY, &my_mutex) {
        // lock held only inside these braces, runs only if acquired
}
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 守卫类型名称（Guard Type Name），由 SCOPE_COND_GUARD_DEFINE 定义。 |
| `_fail` | 无法获取锁时执行的语句（Statement），例如 break、return -EBUSY，或使用 {} 静默跳过代码块。 |
| `...` | 用于获取守卫（Acquire Guard）的参数，例如锁对象。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_SCOPE_CLEANUP_HELPERS 时可用。

<a id="gad7807c92614173dacfe7af2ca6a572ab"></a>

### `scoped_guard`

```c
#define scoped_guard ( _name, ... )
```

```c
#include <zephyr/cleanup.h>
```

展开值（Value）：

```c
Z_SCOPED_GUARD(_name, Z_UNIQUE_ID(scoped_g), Z_UNIQUE_ID(scoped_done), __VA_ARGS__)
```

为随后代码块的生命周期（Lifetime）获取守卫（Guard）。

此宏获取一个作用域守卫锁（Scoped Guard Lock），并在紧随其后的花括号代码块期间持有它，离开代码块时立即释放。scope_guard 的守卫持续到外围作用域结束，而这里创建的守卫绑定于它自己的代码块。

代码块恰好执行一次。以任何方式离开代码块都会释放锁，包括 break、return 和 goto。注意，该代码块使用隐藏循环（Hidden Loop）实现，因此 break 和 continue 都会离开受守卫保护的代码块，而不会作用于外围循环。

此宏也接受通过 SCOPE_COND_GUARD_DEFINE 定义的守卫（Guard）。此时若无法获取锁，则跳过代码块，也不持有任何锁；如果需要在获取失败时执行语句，请使用 scoped_cond_guard。

用法（Usage）：

原始示例（Example）：

```c
scoped_guard(k_mutex, &my_mutex) {
        // lock held only inside these braces
}
// lock released here
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 守卫类型名称（Guard Type Name），由 SCOPE_GUARD_DEFINE 或 SCOPE_COND_GUARD_DEFINE 定义。 |
| `...` | 用于获取守卫（Acquire Guard）的参数，例如锁对象。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_SCOPE_CLEANUP_HELPERS 时可用。


## 6.3\_原页交叉引用（Cross References）

- [zephyr/cleanup.h](../api_file_system_power_reference/P005_zephyr__cleanup.h_文件参考.md)
- [CONFIG_SCOPE_CLEANUP_HELPERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SCOPE_CLEANUP_HELPERS)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [k_mutex_lock](../synchronization_reference/P006_互斥量公共接口.md#ga850549358645249c285669baa49c33b0)
- [K_NO_WAIT](../timer_reference/P086_系统时钟公共接口.md#ga3d9541cfe2e8395af66d186efa77362f)
- [k_mutex_unlock](../synchronization_reference/P006_互斥量公共接口.md#ga360f4c0e7258b0d7030cdb1f452b2c31)
- [COND_CODE_0](../util_reference/P001_通用工具公共接口.md#ga5483ea38af79bc6c4509936288705377)
- [NUM_VA_ARGS](../util_reference/P001_通用工具公共接口.md#ga1e5b59140ab2bf4471a512b689eda2cb)
- [k_free](../heap_reference/P001_内核堆公共接口.md#ga79b63cc93b3358cf82d74f40e73b69d5)
- [K_FOREVER](../timer_reference/P086_系统时钟公共接口.md#ga0bb4b83f0222193b21a8910311bab0ca)
- [k_malloc](../heap_reference/P001_内核堆公共接口.md#gaa8edf1e63e5d5dd78d7adcfd787394ee)
- [ENOMEM](../error_reference/P003_系统错误号公共接口.md#ga6a05c923dad0c1208043e9c20a58c8e5)
- [printk](../api_file_clock_network_reference/P019_zephyr__sys__printk.h_文件参考.md#a1bce54a738ce2d9dd6d95ee842ec237c)
- [EBUSY](../error_reference/P003_系统错误号公共接口.md#ga8368025077a0385849d6817b2007c095)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__cleanup__interface_html_ga4faf2c585a3fa2ce28480a5e2805ca8b"></a>
<a id="agroup__cleanup__interface_html_ga88752a55762b11e721c3052c6adc401a"></a>
<a id="agroup__clock__apis_html_ga3d9541cfe2e8395af66d186efa77362f"></a>
<a id="agroup__mutex__apis_html_ga360f4c0e7258b0d7030cdb1f452b2c31"></a>
<a id="agroup__mutex__apis_html_ga850549358645249c285669baa49c33b0"></a>
<a id="astructk__mutex_html"></a>
<a id="agroup__cleanup__interface_html_ga62362f13860dbea4361e7cf149801d3f"></a>
<a id="agroup__cleanup__interface_html_ga5ea0ef9eed956fa112b069d87f8b05e5"></a>
<a id="agroup__sys-util_html_ga1e5b59140ab2bf4471a512b689eda2cb"></a>
<a id="agroup__sys-util_html_ga5483ea38af79bc6c4509936288705377"></a>
<a id="agroup__cleanup__interface_html_ga07847cc6bb3cd5f63b4d05e084eb9203"></a>
<a id="agroup__heap__apis_html_ga79b63cc93b3358cf82d74f40e73b69d5"></a>
<a id="agroup__cleanup__interface_html_ga3905160905199178d29b66084f237f4e"></a>
<a id="agroup__cleanup__interface_html_gab584b9adf45e13376c0f8e0b817a6213"></a>
<a id="agroup__clock__apis_html_ga0bb4b83f0222193b21a8910311bab0ca"></a>
<a id="agroup__heap__apis_html_gaa8edf1e63e5d5dd78d7adcfd787394ee"></a>
<a id="agroup__system__errno_html_ga6a05c923dad0c1208043e9c20a58c8e5"></a>
<a id="aprintk_8h_html_a1bce54a738ce2d9dd6d95ee842ec237c"></a>
<a id="agroup__cleanup__interface_html_ga096c421f2ba9d7acd68039d493a80b63"></a>
<a id="agroup__cleanup__interface_html_ga1f5c0f74610d1bbcc1fd3c7914ab9a7c"></a>
<a id="agroup__system__errno_html_ga8368025077a0385849d6817b2007c095"></a>
<a id="agroup__cleanup__interface_html_gad7807c92614173dacfe7af2ca6a572ab"></a>

---

[上一章](P005_子网配置（Subnet Configuration）.md) · [返回大纲](大纲.md) · [下一章](P007_Silicon Labs SiWx91x 时钟标识符（Clock identifiers）.md)
