---
id: learning.zephyr-docs.api-file-management-reference.page-39
title: zephyr__dt-bindings__reserved-memory__nordic-owned-memory.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nordic-owned-memory_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_zephyr\_\_dt-bindings\_\_reserved-memory\_\_nordic-owned-memory.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nordic-owned-memory_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 39.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 基本内存权限标志（Basic memory permission flags）

<a id="r_af64e25183317e21ccb2499c97d9afdff"></a>

```c
#define NRF_PERM_R BIT(0)
```

相关声明：[NRF_PERM_R](#af64e25183317e21ccb2499c97d9afdff)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

可读（Readable）。

<a id="r_a0c02f911d592b79403024ff6ae924dad"></a>

```c
#define NRF_PERM_W BIT(1)
```

相关声明：[NRF_PERM_W](#a0c02f911d592b79403024ff6ae924dad)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

可写（Writable）。

<a id="r_a5e9cae0aa74888ed91dd7c3ffef23ec2"></a>

```c
#define NRF_PERM_X BIT(2)
```

相关声明：[NRF_PERM_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

可执行（Executable）。

<a id="r_a8e96aeef751fbb1c3bf2bdee474ea097"></a>

```c
#define NRF_PERM_S BIT(3)
```

相关声明：[NRF_PERM_S](#a8e96aeef751fbb1c3bf2bdee474ea097)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

仅安全域（Secure-only）。

<a id="r_a758490f83493121bfc04445af185efed"></a>

```c
#define NRF_PERM_NSC BIT(4)
```

相关声明：[NRF_PERM_NSC](#a758490f83493121bfc04445af185efed)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

可由非安全域调用（Non-secure-callable）。

<a id="define-members-1"></a>

### 内存权限标志组合（Memory permission flag combinations）

注意：`NRF_PERM_NSC` 会覆盖所有其他标志，因此此处不包含它。

<a id="r_ae977886b6f509bcda34b3864cf5b06e2"></a>

```c
#define NRF_PERM_RW (NRF_PERM_R | NRF_PERM_W)
```

相关声明：[NRF_PERM_RW](#ae977886b6f509bcda34b3864cf5b06e2)、[NRF_PERM_R](#af64e25183317e21ccb2499c97d9afdff)、[NRF_PERM_W](#a0c02f911d592b79403024ff6ae924dad)。

<a id="r_a7de269dc15b92b49d3b865cd00dcb66e"></a>

```c
#define NRF_PERM_RX (NRF_PERM_R | NRF_PERM_X)
```

相关声明：[NRF_PERM_RX](#a7de269dc15b92b49d3b865cd00dcb66e)、[NRF_PERM_R](#af64e25183317e21ccb2499c97d9afdff)、[NRF_PERM_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2)。

<a id="r_adbc1087aa45ce5a82562b76e703422f6"></a>

```c
#define NRF_PERM_RS (NRF_PERM_R | NRF_PERM_S)
```

相关声明：[NRF_PERM_RS](#adbc1087aa45ce5a82562b76e703422f6)、[NRF_PERM_R](#af64e25183317e21ccb2499c97d9afdff)、[NRF_PERM_S](#a8e96aeef751fbb1c3bf2bdee474ea097)。

<a id="r_af7f291c2ca6d2c9366f123b229dcddeb"></a>

```c
#define NRF_PERM_WX (NRF_PERM_W | NRF_PERM_X)
```

相关声明：[NRF_PERM_WX](#af7f291c2ca6d2c9366f123b229dcddeb)、[NRF_PERM_W](#a0c02f911d592b79403024ff6ae924dad)、[NRF_PERM_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2)。

<a id="r_af7592990797753acf9e035e9a226b20a"></a>

```c
#define NRF_PERM_WS (NRF_PERM_W | NRF_PERM_S)
```

相关声明：[NRF_PERM_WS](#af7592990797753acf9e035e9a226b20a)、[NRF_PERM_W](#a0c02f911d592b79403024ff6ae924dad)、[NRF_PERM_S](#a8e96aeef751fbb1c3bf2bdee474ea097)。

<a id="r_a98ec396cd8e0918c730607ee100bf76c"></a>

```c
#define NRF_PERM_XS (NRF_PERM_X | NRF_PERM_S)
```

相关声明：[NRF_PERM_XS](#a98ec396cd8e0918c730607ee100bf76c)、[NRF_PERM_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2)、[NRF_PERM_S](#a8e96aeef751fbb1c3bf2bdee474ea097)。

<a id="r_a5e83619291670695a30b72232ba51d2d"></a>

```c
#define NRF_PERM_RWX (NRF_PERM_R | NRF_PERM_W | NRF_PERM_X)
```

相关声明：[NRF_PERM_RWX](#a5e83619291670695a30b72232ba51d2d)、[NRF_PERM_R](#af64e25183317e21ccb2499c97d9afdff)、[NRF_PERM_W](#a0c02f911d592b79403024ff6ae924dad)、[NRF_PERM_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2)。

<a id="r_a0967ce2b4641901b0f002eb3d0134eed"></a>

```c
#define NRF_PERM_RWS (NRF_PERM_R | NRF_PERM_W | NRF_PERM_S)
```

相关声明：[NRF_PERM_RWS](#a0967ce2b4641901b0f002eb3d0134eed)、[NRF_PERM_R](#af64e25183317e21ccb2499c97d9afdff)、[NRF_PERM_W](#a0c02f911d592b79403024ff6ae924dad)、[NRF_PERM_S](#a8e96aeef751fbb1c3bf2bdee474ea097)。

<a id="r_aee7d5b93a610deca9a6aa66314ed664c"></a>

```c
#define NRF_PERM_RXS (NRF_PERM_R | NRF_PERM_X | NRF_PERM_S)
```

相关声明：[NRF_PERM_RXS](#aee7d5b93a610deca9a6aa66314ed664c)、[NRF_PERM_R](#af64e25183317e21ccb2499c97d9afdff)、[NRF_PERM_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2)、[NRF_PERM_S](#a8e96aeef751fbb1c3bf2bdee474ea097)。

<a id="r_a4b8d7cae0009bbaa43b181389ae37d01"></a>

```c
#define NRF_PERM_WXS (NRF_PERM_W | NRF_PERM_X | NRF_PERM_S)
```

相关声明：[NRF_PERM_WXS](#a4b8d7cae0009bbaa43b181389ae37d01)、[NRF_PERM_W](#a0c02f911d592b79403024ff6ae924dad)、[NRF_PERM_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2)、[NRF_PERM_S](#a8e96aeef751fbb1c3bf2bdee474ea097)。

<a id="r_a5ef62494ad09d23f0f2d35ffc7d7c91e"></a>

```c
#define NRF_PERM_RWXS (NRF_PERM_R | NRF_PERM_W | NRF_PERM_X | NRF_PERM_S)
```

相关声明：[NRF_PERM_RWXS](#a5ef62494ad09d23f0f2d35ffc7d7c91e)、[NRF_PERM_R](#af64e25183317e21ccb2499c97d9afdff)、[NRF_PERM_W](#a0c02f911d592b79403024ff6ae924dad)、[NRF_PERM_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2)、[NRF_PERM_S](#a8e96aeef751fbb1c3bf2bdee474ea097)。

## 39.2\_详细说明（Detailed Documentation）

<a id="a758490f83493121bfc04445af185efed"></a>

### `NRF_PERM_NSC`

```c
#define NRF_PERM_NSC BIT(4)
```

可由非安全域调用（Non-secure-callable）。

<a id="af64e25183317e21ccb2499c97d9afdff"></a>

### `NRF_PERM_R`

```c
#define NRF_PERM_R BIT(0)
```

可读（Readable）。

<a id="adbc1087aa45ce5a82562b76e703422f6"></a>

### `NRF_PERM_RS`

```c
#define NRF_PERM_RS (NRF_PERM_R | NRF_PERM_S)
```

<a id="ae977886b6f509bcda34b3864cf5b06e2"></a>

### `NRF_PERM_RW`

```c
#define NRF_PERM_RW (NRF_PERM_R | NRF_PERM_W)
```

<a id="a0967ce2b4641901b0f002eb3d0134eed"></a>

### `NRF_PERM_RWS`

```c
#define NRF_PERM_RWS (NRF_PERM_R | NRF_PERM_W | NRF_PERM_S)
```

<a id="a5e83619291670695a30b72232ba51d2d"></a>

### `NRF_PERM_RWX`

```c
#define NRF_PERM_RWX (NRF_PERM_R | NRF_PERM_W | NRF_PERM_X)
```

<a id="a5ef62494ad09d23f0f2d35ffc7d7c91e"></a>

### `NRF_PERM_RWXS`

```c
#define NRF_PERM_RWXS (NRF_PERM_R | NRF_PERM_W | NRF_PERM_X | NRF_PERM_S)
```

<a id="a7de269dc15b92b49d3b865cd00dcb66e"></a>

### `NRF_PERM_RX`

```c
#define NRF_PERM_RX (NRF_PERM_R | NRF_PERM_X)
```

<a id="aee7d5b93a610deca9a6aa66314ed664c"></a>

### `NRF_PERM_RXS`

```c
#define NRF_PERM_RXS (NRF_PERM_R | NRF_PERM_X | NRF_PERM_S)
```

<a id="a8e96aeef751fbb1c3bf2bdee474ea097"></a>

### `NRF_PERM_S`

```c
#define NRF_PERM_S BIT(3)
```

仅安全域（Secure-only）。

<a id="a0c02f911d592b79403024ff6ae924dad"></a>

### `NRF_PERM_W`

```c
#define NRF_PERM_W BIT(1)
```

可写（Writable）。

<a id="af7592990797753acf9e035e9a226b20a"></a>

### `NRF_PERM_WS`

```c
#define NRF_PERM_WS (NRF_PERM_W | NRF_PERM_S)
```

<a id="af7f291c2ca6d2c9366f123b229dcddeb"></a>

### `NRF_PERM_WX`

```c
#define NRF_PERM_WX (NRF_PERM_W | NRF_PERM_X)
```

<a id="a4b8d7cae0009bbaa43b181389ae37d01"></a>

### `NRF_PERM_WXS`

```c
#define NRF_PERM_WXS (NRF_PERM_W | NRF_PERM_X | NRF_PERM_S)
```

<a id="a5e9cae0aa74888ed91dd7c3ffef23ec2"></a>

### `NRF_PERM_X`

```c
#define NRF_PERM_X BIT(2)
```

可执行（Executable）。

<a id="a98ec396cd8e0918c730607ee100bf76c"></a>

### `NRF_PERM_XS`

```c
#define NRF_PERM_XS (NRF_PERM_X | NRF_PERM_S)
```


## 39.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P586_nordic-owned-memory.h_源码浏览.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P038_zephyr__net__net_time.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P040_zephyr__drivers__interrupt_controller__nxp_irqsteer.h_文件参考.md)
