---
id: learning.zephyr-docs.api-file-configuration-reference.page-24
title: zephyr__drivers__emul_stub_device.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/emul__stub__device_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_zephyr\_\_drivers\_\_emul\_stub\_device.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/emul__stub__device_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

为没有对应驱动的仿真器提供占位设备支持（Stub Device Support）。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
```

查看此文件的源码。

为没有对应驱动的仿真器提供占位设备支持（Stub Device Support）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 24.1\_宏定义（Macros）

<a id="r_ae42dec3fd3ebdfc8ab5c1b9eabea26d0"></a>

```c
#define EMUL_STUB_DEVICE(n)
```

相关声明：[EMUL_STUB_DEVICE](#ae42dec3fd3ebdfc8ab5c1b9eabea26d0)。

为仿真器实例（Emulator Instance）提供桩设备（Stub Device）。

## 24.2\_详细说明（Detailed Documentation）

<a id="ae42dec3fd3ebdfc8ab5c1b9eabea26d0"></a>

### `EMUL_STUB_DEVICE`

```c
#define EMUL_STUB_DEVICE ( n)
```

展开值（Value）：

```c
__maybe_unused static int emul_init_stub_##n(const struct device *dev)                     \
{                                                                                          \
        ARG_UNUSED(dev);                                                                   \
        return 0;                                                                          \
}                                                                                          \
                                                                                           \
static struct emul_stub_dev_data stub_data_##n;                                            \
static struct emul_stub_dev_config stub_config_##n;                                        \
static struct emul_stub_dev_api stub_api_##n;                                              \
DEVICE_DT_INST_DEFINE(n, &emul_init_stub_##n, NULL, &stub_data_##n, &stub_config_##n,      \
                      POST_KERNEL, CONFIG_KERNEL_INIT_PRIORITY_DEVICE, &stub_api_##n);
```

为仿真器实例（Emulator Instance）提供桩设备（Stub Device）。

为 `DT_DRV_COMPAT` 的每个实例定义桩设备（Stub Device），以便仿真器（Emulator）的设备树节点（Devicetree Node）具有对应的设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `n` | DT_DRV_COMPAT实例编号（Instance Number）。 |


## 24.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [查看此文件的源码。](../api_source_configuration_reference/P022_emul_stub_device.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astructdevice_html"></a>

---

[上一章](P023_zephyr__drivers__emul_fuel_gauge.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P025_zephyr__drivers__sensor__ens160.h_文件参考.md)
