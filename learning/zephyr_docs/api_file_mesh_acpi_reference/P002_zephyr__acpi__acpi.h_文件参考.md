---
id: learning.zephyr-docs.api-file-mesh-acpi-reference.page-2
title: zephyr__acpi__acpi.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_acpi\_\_acpi.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <acpica/source/include/acpi.h>
#include <zephyr/drivers/pcie/pcie.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_acpi_5Fdev"></a>

```c
struct acpi_dev
```

相关声明：[acpi_dev](../driver_model_reference/P001_ACPI设备.md)。

<a id="r_acpi_5Fdmar_5Fid"></a>

```c
union acpi_dmar_id
```

相关声明：[acpi_dmar_id](../platform_security_model_reference/P076_acpi_dmar_id_联合体.md)。

<a id="r_acpi_5Fmcfg"></a>

```c
struct acpi_mcfg
```

相关声明：[acpi_mcfg](../driver_model_reference/P003_ACPI内存配置表.md)。

<a id="r_acpi_5Firq_5Fresource"></a>

```c
struct acpi_irq_resource
```

相关声明：[acpi_irq_resource](../driver_model_reference/P002_ACPI中断资源.md)。

<a id="r_acpi_5Freg_5Fbase"></a>

```c
struct acpi_reg_base
```

相关声明：[acpi_reg_base](../driver_model_reference/P005_ACPI寄存器基址.md)。

<a id="r_acpi_5Fmmio_5Fresource"></a>

```c
struct acpi_mmio_resource
```

相关声明：[acpi_mmio_resource](../driver_model_reference/P004_ACPI内存映射资源.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_a5de2990466b70b703d48c6c341e427b3"></a>

```c
#define ACPI_RES_INVALID ACPI_RESOURCE_TYPE_MAX
```

相关声明：[ACPI_RES_INVALID](#a5de2990466b70b703d48c6c341e427b3)。

<a id="r_a9f534875dab25e2ea48b2676ea8e71b8"></a>

```c
#define ACPI_DRHD_FLAG_INCLUDE_PCI_ALL BIT(0)
```

相关声明：[ACPI_DRHD_FLAG_INCLUDE_PCI_ALL](#a9f534875dab25e2ea48b2676ea8e71b8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a92085a7267a8f1569d6d836fc6f8459b"></a>

```c
#define ACPI_DMAR_FLAG_INTR_REMAP BIT(0)
```

相关声明：[ACPI_DMAR_FLAG_INTR_REMAP](#a92085a7267a8f1569d6d836fc6f8459b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a346ee226be8400feaf94198db3da4c44"></a>

```c
#define ACPI_DMAR_FLAG_X2APIC_OPT_OUT BIT(1)
```

相关声明：[ACPI_DMAR_FLAG_X2APIC_OPT_OUT](#a346ee226be8400feaf94198db3da4c44)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a695794eaf1ebfa25ed1c0ad0d42105f2"></a>

```c
#define ACPI_DMAR_FLAG_DMA_CTRL_PLATFORM_OPT_IN BIT(2)
```

相关声明：[ACPI_DMAR_FLAG_DMA_CTRL_PLATFORM_OPT_IN](#a695794eaf1ebfa25ed1c0ad0d42105f2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a1f8ab630f3c98ceb0c9f59a78b9a24da"></a>

```c
#define ACPI_MMIO_GET(res)
```

相关声明：[ACPI_MMIO_GET](#a1f8ab630f3c98ceb0c9f59a78b9a24da)。

<a id="r_a0d45750fe126a6f9641f7f94d843381d"></a>

```c
#define ACPI_IO_GET(res)
```

相关声明：[ACPI_IO_GET](#a0d45750fe126a6f9641f7f94d843381d)。

<a id="r_abc9aa4017edfc68ac47208e8f758dd60"></a>

```c
#define ACPI_RESOURCE_SIZE_GET(res)
```

相关声明：[ACPI_RESOURCE_SIZE_GET](#abc9aa4017edfc68ac47208e8f758dd60)。

<a id="r_aa822c0ca234e1b3ea5fc0007c9f490d4"></a>

```c
#define ACPI_RESOURCE_TYPE_GET(res)
```

相关声明：[ACPI_RESOURCE_TYPE_GET](#aa822c0ca234e1b3ea5fc0007c9f490d4)。

<a id="r_af131fc0845a57664d8df8983c074c064"></a>

```c
#define ACPI_MULTI_MMIO_GET(res, idx)
```

相关声明：[ACPI_MULTI_MMIO_GET](#af131fc0845a57664d8df8983c074c064)。

<a id="r_ad5adfc6540aa9118542970d76d6512bd"></a>

```c
#define ACPI_MULTI_IO_GET(res, idx)
```

相关声明：[ACPI_MULTI_IO_GET](#ad5adfc6540aa9118542970d76d6512bd)。

<a id="r_ac77fc44c979b87bcb571f77657954d99"></a>

```c
#define ACPI_MULTI_RESOURCE_SIZE_GET(res, idx)
```

相关声明：[ACPI_MULTI_RESOURCE_SIZE_GET](#ac77fc44c979b87bcb571f77657954d99)。

<a id="r_a1e50c8e8f08f6bab0ed12ad97f573b0f"></a>

```c
#define ACPI_MULTI_RESOURCE_TYPE_GET(res, idx)
```

相关声明：[ACPI_MULTI_RESOURCE_TYPE_GET](#a1e50c8e8f08f6bab0ed12ad97f573b0f)。

<a id="r_ac174fef6e234ec8452485c199d9de90d"></a>

```c
#define ACPI_RESOURCE_COUNT_GET(res)
```

相关声明：[ACPI_RESOURCE_COUNT_GET](#ac174fef6e234ec8452485c199d9de90d)。

<a id="r_a76212438f3a5020919bfde46128f2fb4"></a>

```c
#define ACPI_DT_HID(node_id)
```

相关声明：[ACPI_DT_HID](#a76212438f3a5020919bfde46128f2fb4)。

获取节点的高级配置与电源接口硬件标识符（ACPI Hardware ID，HID）。

<a id="r_a509335d1d6310b109a5047c5a65e1761"></a>

```c
#define ACPI_DT_UID(node_id)
```

相关声明：[ACPI_DT_UID](#a509335d1d6310b109a5047c5a65e1761)。

获取节点的 ACPI 唯一标识符（Unique ID，UID），如果存在。

<a id="r_a9b849938061877cee953fd7257575268"></a>

```c
#define ACPI_DT_HAS_HID(node_id)
```

相关声明：[ACPI_DT_HAS_HID](#a9b849938061877cee953fd7257575268)。

检查节点是否具有 ACPI 硬件标识符（HID）属性。

<a id="r_ad91001baf45a0110c85c51b405beaced"></a>

```c
#define ACPI_DT_HAS_UID(node_id)
```

相关声明：[ACPI_DT_HAS_UID](#ad91001baf45a0110c85c51b405beaced)。

检查节点是否具有 ACPI 唯一标识符（UID）属性。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.3\_类型定义（Typedefs）

<a id="r_af675794f8aa74fb58c7a2c7266f05357"></a>

```c
typedef void(* dmar_foreach_subtable_func_t) (ACPI_DMAR_HEADER *subtable, void *arg)
```

相关声明：[dmar_foreach_subtable_func_t](#af675794f8aa74fb58c7a2c7266f05357)。

<a id="r_a6b294403ca4a5e1c234c42279d201490"></a>

```c
typedef void(* dmar_foreach_devscope_func_t) (ACPI_DMAR_DEVICE_SCOPE *devscope, void *arg)
```

相关声明：[dmar_foreach_devscope_func_t](#a6b294403ca4a5e1c234c42279d201490)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.4\_枚举（Enumerations）

<a id="r_a225bfac5f9770bd826ae98d2bbbbfc5b"></a>

```c
enum acpi_res_type { ACPI_RES_TYPE_IO , ACPI_RES_TYPE_MEM , ACPI_RES_TYPE_UNKNOWN }
```

相关声明：[acpi_res_type](#a225bfac5f9770bd826ae98d2bbbbfc5b)、[ACPI_RES_TYPE_IO](#a225bfac5f9770bd826ae98d2bbbbfc5badde21e335fe3363fd60eb3076dfe7a9f)、[ACPI_RES_TYPE_MEM](#a225bfac5f9770bd826ae98d2bbbbfc5ba609d72a263b7ed46da533aeab6255626)、[ACPI_RES_TYPE_UNKNOWN](#a225bfac5f9770bd826ae98d2bbbbfc5bad9f5eaef7ee5ef391c917786a358278b)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.5\_函数（Functions）

<a id="r_ac97acaf39d481f3c3915c763e7f2cdc3"></a>

```c
int acpi_legacy_irq_init (const char *hid, const char *uid)
```

相关声明：[acpi_legacy_irq_init](#ac97acaf39d481f3c3915c763e7f2cdc3)。

从 ACPI 初始化传统中断路由表（Legacy Interrupt Routing Table）信息。

<a id="r_a139f52f8431a00d34abae1d5a5f31d92"></a>

```c
uint32_t acpi_legacy_irq_get (pcie_bdf_t bdf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[acpi_legacy_irq_get](#a139f52f8431a00d34abae1d5a5f31d92)、[pcie_bdf_t](../api_memory_timer_topic_reference/P008_PCIe 主机（PCIe Host）.md#gaf9748042a4f3c8d912d19df1ccf737fb)。

获取 PCI 设备的传统中断号（Legacy Interrupt Number）。

<a id="r_ae8d0e92bc9f94d1c70dc893b686c29de"></a>

```c
int acpi_current_resource_get (char *dev_name, ACPI_RESOURCE **res)
```

相关声明：[acpi_current_resource_get](#ae8d0e92bc9f94d1c70dc893b686c29de)。

获取设备的当前资源设置（Current Resource Settings）。

<a id="r_a5787a05051ffb4ccab113cf2e834678d"></a>

```c
int acpi_possible_resource_get (char *dev_name, ACPI_RESOURCE **res)
```

相关声明：[acpi_possible_resource_get](#a5787a05051ffb4ccab113cf2e834678d)。

获取设备可能的资源设置（Possible Resource Settings）。

<a id="r_a703f435a640e34080a6cf52c2256294e"></a>

```c
int acpi_current_resource_free (ACPI_RESOURCE *res)
```

相关声明：[acpi_current_resource_free](#a703f435a640e34080a6cf52c2256294e)。

释放通过 `acpi_current_resource_get()` 获取的当前资源列表内存。

<a id="r_aa5d7b0c25e6e2767c15edbce33971c72"></a>

```c
ACPI_RESOURCE * acpi_resource_parse (ACPI_RESOURCE *res, int res_type)
```

相关声明：[acpi_resource_parse](#aa5d7b0c25e6e2767c15edbce33971c72)。

按给定资源类型（Resource Type）解析资源表。

<a id="r_a6416a93af8385d3784d205b8811a6a94"></a>

```c
struct acpi_dev * acpi_device_get (const char *hid, const char *uid)
```

相关声明：[acpi_dev](../driver_model_reference/P001_ACPI设备.md)、[acpi_device_get](#a6416a93af8385d3784d205b8811a6a94)。

按给定硬件标识符（Hardware ID）和唯一标识符（Unique ID）获取 ACPI 设备信息。

<a id="r_a625d35bab5922b679517fe8d8b0aface"></a>

```c
struct acpi_dev * acpi_device_by_index_get (int index)
```

相关声明：[acpi_dev](../driver_model_reference/P001_ACPI设备.md)、[acpi_device_by_index_get](#a625d35bab5922b679517fe8d8b0aface)。

按索引获取 ACPI 设备信息（Device Info）。

<a id="r_a3a0c7a6232c1f1f08ae0be3e5c3fac7a"></a>

```c
static ACPI_RESOURCE_IRQ * acpi_irq_res_get (ACPI_RESOURCE *res_lst)
```

相关声明：[acpi_irq_res_get](#a3a0c7a6232c1f1f08ae0be3e5c3fac7a)。

解析资源表以获得中断请求（IRQ）信息。

<a id="r_ab8a0982a3acc857ea059bb617b8b43f7"></a>

```c
int acpi_device_irq_get (struct acpi_dev *child_dev, struct acpi_irq_resource *irq_res)
```

相关声明：[acpi_device_irq_get](#ab8a0982a3acc857ea059bb617b8b43f7)、[acpi_dev](../driver_model_reference/P001_ACPI设备.md)、[child_dev](../api_buffer_paging_topic_reference/P012_MFD ADP5360 接口.md#gae4d56fd30130dc4f332ecf43465a1558)、[acpi_irq_resource](../driver_model_reference/P002_ACPI中断资源.md)。

解析资源表以获得中断请求（IRQ）信息。

<a id="r_a4179d931233431ec61b5e12c1c77931d"></a>

```c
int acpi_device_mmio_get (struct acpi_dev *child_dev, struct acpi_mmio_resource *mmio_res)
```

相关声明：[acpi_device_mmio_get](#a4179d931233431ec61b5e12c1c77931d)、[acpi_dev](../driver_model_reference/P001_ACPI设备.md)、[child_dev](../api_buffer_paging_topic_reference/P012_MFD ADP5360 接口.md#gae4d56fd30130dc4f332ecf43465a1558)、[acpi_mmio_resource](../driver_model_reference/P004_ACPI内存映射资源.md)。

解析资源表以获得内存映射 I/O（MMIO）信息。

<a id="r_a44b747b1b7493627a8022c49571b04ff"></a>

```c
int acpi_device_type_get (ACPI_RESOURCE *res)
```

相关声明：[acpi_device_type_get](#a44b747b1b7493627a8022c49571b04ff)。

解析资源表以识别资源类型（Resource Type）。

<a id="r_ab6f0b5f0ae6cf1da923051f2e38fa193"></a>

```c
void * acpi_table_get (char *signature, int inst)
```

相关声明：[acpi_table_get](#ab6f0b5f0ae6cf1da923051f2e38fa193)。

获取与给定签名（Signature）对应的 ACPI 表。

<a id="r_abb83809ce252f82f93ea042dfba3fbfd"></a>

```c
int acpi_madt_entry_get (int type, ACPI_SUBTABLE_HEADER **tables, int *num_inst)
```

相关声明：[acpi_madt_entry_get](#abb83809ce252f82f93ea042dfba3fbfd)。

获取给定类型的 ACPI MAD 表（MAD Table）。

<a id="r_a36d899259fe64aea46549e54ebbfbf0a"></a>

```c
int acpi_dmar_entry_get (enum AcpiDmarType type, ACPI_SUBTABLE_HEADER **tables)
```

相关声明：[acpi_dmar_entry_get](#a36d899259fe64aea46549e54ebbfbf0a)。

获取给定类型的 DMA 重映射结构（DMA Remapping Structure）。

<a id="r_a1d9f2e00bbcc8a0e101091c6d6be4ac5"></a>

```c
int acpi_drhd_get (enum AcpiDmarScopeType scope, ACPI_DMAR_DEVICE_SCOPE *dev_scope, union acpi_dmar_id *dmar_id, int *num_inst, int max_inst)
```

相关声明：[acpi_drhd_get](#a1d9f2e00bbcc8a0e101091c6d6be4ac5)、[acpi_dmar_id](../platform_security_model_reference/P076_acpi_dmar_id_联合体.md)。

获取给定作用域（Scope）的 ACPI DMA 重映射硬件单元定义（DRHD）信息。

<a id="r_af62e15025d3442b2db39b34c3e138671"></a>

```c
void acpi_dmar_foreach_subtable (ACPI_TABLE_DMAR *dmar, dmar_foreach_subtable_func_t func, void *arg)
```

相关声明：[acpi_dmar_foreach_subtable](#af62e15025d3442b2db39b34c3e138671)、[dmar_foreach_subtable_func_t](#af675794f8aa74fb58c7a2c7266f05357)。

<a id="r_a77d02fbe12ff3e02368582c489f7c7d5"></a>

```c
void acpi_dmar_foreach_devscope (ACPI_DMAR_HARDWARE_UNIT *hu, dmar_foreach_devscope_func_t func, void *arg)
```

相关声明：[acpi_dmar_foreach_devscope](#a77d02fbe12ff3e02368582c489f7c7d5)、[dmar_foreach_devscope_func_t](#a6b294403ca4a5e1c234c42279d201490)。

<a id="r_a9768a4b3d13edb8456736256ec015e04"></a>

```c
int acpi_dmar_ioapic_get (uint16_t *ioapic_id)
```

相关声明：[acpi_dmar_ioapic_get](#a9768a4b3d13edb8456736256ec015e04)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取 I/O 高级可编程中断控制器标识符（IOAPIC ID）。

<a id="r_a750b6348bfc9f3867b561ff9d7a08b4c"></a>

```c
ACPI_MADT_LOCAL_APIC * acpi_local_apic_get (int cpu_num)
```

相关声明：[acpi_local_apic_get](#a750b6348bfc9f3867b561ff9d7a08b4c)。

获取第 `n` 个已启用的本地高级可编程中断控制器（Local APIC）信息。

<a id="r_a379137f6a7b2a62e952dd961d0b5ed25"></a>

```c
ACPI_MADT_LOCAL_X2APIC * acpi_local_x2apic_get (int cpu_num)
```

相关声明：[acpi_local_x2apic_get](#a379137f6a7b2a62e952dd961d0b5ed25)。

获取第 `n` 个已启用的本地 x2APIC 信息（MADT 类型 9）。

<a id="r_aab272d92004e687bdd2936f648f3f9f9"></a>

```c
int acpi_invoke_method (char *path, ACPI_OBJECT_LIST *arg_list, ACPI_OBJECT *ret_obj)
```

相关声明：[acpi_invoke_method](#aab272d92004e687bdd2936f648f3f9f9)。

调用 ACPI 方法（Method）并返回结果。

<a id="r_afaad7277ab95c5d5cbf2d66407cdc7fa"></a>

```c
int acpi_poweroff (void)
```

相关声明：[acpi_poweroff](#afaad7277ab95c5d5cbf2d66407cdc7fa)。

将系统设为软关机（Soft Off）状态，以执行系统级关机。

## 2.6\_详细说明（Detailed Documentation）

<a id="a695794eaf1ebfa25ed1c0ad0d42105f2"></a>

### `ACPI_DMAR_FLAG_DMA_CTRL_PLATFORM_OPT_IN`

```c
#define ACPI_DMAR_FLAG_DMA_CTRL_PLATFORM_OPT_IN BIT(2)
```

<a id="a92085a7267a8f1569d6d836fc6f8459b"></a>

### `ACPI_DMAR_FLAG_INTR_REMAP`

```c
#define ACPI_DMAR_FLAG_INTR_REMAP BIT(0)
```

<a id="a346ee226be8400feaf94198db3da4c44"></a>

### `ACPI_DMAR_FLAG_X2APIC_OPT_OUT`

```c
#define ACPI_DMAR_FLAG_X2APIC_OPT_OUT BIT(1)
```

<a id="a9f534875dab25e2ea48b2676ea8e71b8"></a>

### `ACPI_DRHD_FLAG_INCLUDE_PCI_ALL`

```c
#define ACPI_DRHD_FLAG_INCLUDE_PCI_ALL BIT(0)
```

<a id="a9b849938061877cee953fd7257575268"></a>

### `ACPI_DT_HAS_HID`

```c
#define ACPI_DT_HAS_HID ( node_id)
```

展开值（Value）：

```c
DT_NODE_HAS_PROP(node_id, acpi_hid)
```

检查节点是否具有 ACPI 硬件标识符（HID）属性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | DTS节点标识符。 |

**返回（Returns）**：返回值（Returns）：节点具有 HID 时为 1，否则为 0。

<a id="ad91001baf45a0110c85c51b405beaced"></a>

### `ACPI_DT_HAS_UID`

```c
#define ACPI_DT_HAS_UID ( node_id)
```

展开值（Value）：

```c
DT_NODE_HAS_PROP(node_id, acpi_uid)
```

检查节点是否具有 ACPI 唯一标识符（UID）属性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | DTS节点标识符。 |

**返回（Returns）**：返回值（Returns）：节点具有 UID 时为 1，否则为 0。

<a id="a76212438f3a5020919bfde46128f2fb4"></a>

### `ACPI_DT_HID`

```c
#define ACPI_DT_HID ( node_id)
```

展开值（Value）：

```c
DT_PROP(node_id, acpi_hid)
```

获取节点的高级配置与电源接口硬件标识符（ACPI Hardware ID，HID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | DTS节点标识符。 |

**返回（Returns）**：返回值（Returns）：ACPI 节点的硬件标识符（HID）。

<a id="a509335d1d6310b109a5047c5a65e1761"></a>

### `ACPI_DT_UID`

```c
#define ACPI_DT_UID ( node_id)
```

展开值（Value）：

```c
DT_PROP_OR(node_id, acpi_uid, NULL)
```

获取节点的 ACPI 唯一标识符（Unique ID，UID），如果存在。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | DTS节点标识符。 |

**返回（Returns）**：返回值（Returns）：ACPI 节点的唯一标识符（UID）；不存在时为 `NULL`。

<a id="a0d45750fe126a6f9641f7f94d843381d"></a>

### `ACPI_IO_GET`

```c
#define ACPI_IO_GET ( res)
```

展开值（Value）：

```c
(res)->reg_base[0].port
```

<a id="a1f8ab630f3c98ceb0c9f59a78b9a24da"></a>

### `ACPI_MMIO_GET`

```c
#define ACPI_MMIO_GET ( res)
```

展开值（Value）：

```c
(res)->reg_base[0].mmio
```

<a id="ad5adfc6540aa9118542970d76d6512bd"></a>

### `ACPI_MULTI_IO_GET`

```c
#define ACPI_MULTI_IO_GET ( res, idx )
```

展开值（Value）：

```c
(res)->reg_base[idx].port
```

<a id="af131fc0845a57664d8df8983c074c064"></a>

### `ACPI_MULTI_MMIO_GET`

```c
#define ACPI_MULTI_MMIO_GET ( res, idx )
```

展开值（Value）：

```c
(res)->reg_base[idx].mmio
```

<a id="ac77fc44c979b87bcb571f77657954d99"></a>

### `ACPI_MULTI_RESOURCE_SIZE_GET`

```c
#define ACPI_MULTI_RESOURCE_SIZE_GET ( res, idx )
```

展开值（Value）：

```c
(res)->reg_base[idx].length
```

<a id="a1e50c8e8f08f6bab0ed12ad97f573b0f"></a>

### `ACPI_MULTI_RESOURCE_TYPE_GET`

```c
#define ACPI_MULTI_RESOURCE_TYPE_GET ( res, idx )
```

展开值（Value）：

```c
(res)->reg_base[idx].type
```

<a id="a5de2990466b70b703d48c6c341e427b3"></a>

### `ACPI_RES_INVALID`

```c
#define ACPI_RES_INVALID ACPI_RESOURCE_TYPE_MAX
```

<a id="ac174fef6e234ec8452485c199d9de90d"></a>

### `ACPI_RESOURCE_COUNT_GET`

```c
#define ACPI_RESOURCE_COUNT_GET ( res)
```

展开值（Value）：

```c
(res)->mmio_max
```

<a id="abc9aa4017edfc68ac47208e8f758dd60"></a>

### `ACPI_RESOURCE_SIZE_GET`

```c
#define ACPI_RESOURCE_SIZE_GET ( res)
```

展开值（Value）：

```c
(res)->reg_base[0].length
```

<a id="aa822c0ca234e1b3ea5fc0007c9f490d4"></a>

### `ACPI_RESOURCE_TYPE_GET`

```c
#define ACPI_RESOURCE_TYPE_GET ( res)
```

展开值（Value）：

```c
(res)->reg_base[0].type
```

<a id="a6b294403ca4a5e1c234c42279d201490"></a>

### `dmar_foreach_devscope_func_t`

```c
typedef void(* dmar_foreach_devscope_func_t) (ACPI_DMAR_DEVICE_SCOPE *devscope, void *arg)
```

<a id="af675794f8aa74fb58c7a2c7266f05357"></a>

### `dmar_foreach_subtable_func_t`

```c
typedef void(* dmar_foreach_subtable_func_t) (ACPI_DMAR_HEADER *subtable, void *arg)
```

<a id="a225bfac5f9770bd826ae98d2bbbbfc5b"></a>

### `acpi_res_type`

```c
enum acpi_res_type
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ACPI_RES_TYPE_IO` | I/O 映射资源类型（I/O-Mapped Resource Type）。 |
| `ACPI_RES_TYPE_MEM` | 内存映射资源类型（Memory-Mapped Resource Type）。 |
| `ACPI_RES_TYPE_UNKNOWN` | 未知资源类型（Unknown Resource Type）。 |

<a id="a703f435a640e34080a6cf52c2256294e"></a>

### `acpi_current_resource_free()`

```c
int acpi_current_resource_free ( ACPI_RESOURCE * res)
```

释放通过 `acpi_current_resource_get()` 获取的当前资源列表内存。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `res` | ACPI 资源列表（Resource List）。 |

**返回（Returns）**：返回值（Returns）：成功时返回 0，否则返回错误码。

<a id="ae8d0e92bc9f94d1c70dc893b686c29de"></a>

### `acpi_current_resource_get()`

```c
int acpi_current_resource_get ( char * dev_name, ACPI_RESOURCE ** res )
```

获取设备的当前资源设置（Current Resource Settings）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev_name` | 设备名称（Device Name）。 |
| `res` | ACPI 资源列表（Resource List）。 |

**返回（Returns）**：返回值（Returns）：成功时返回 0，否则返回错误码。

<a id="a625d35bab5922b679517fe8d8b0aface"></a>

### `acpi_device_by_index_get()`

```c
struct acpi_dev * acpi_device_by_index_get ( int index)
```

按索引获取 ACPI 设备信息（Device Info）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | ACPI 子设备的设备索引（Device Index）。 |

**返回（Returns）**：返回值（Returns）：成功时为 ACPI 子设备信息，否则为 `NULL`。

<a id="a6416a93af8385d3784d205b8811a6a94"></a>

### `acpi_device_get()`

```c
struct acpi_dev * acpi_device_get ( const char * hid, const char * uid )
```

按给定硬件标识符（Hardware ID）和唯一标识符（Unique ID）获取 ACPI 设备信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | ACPI 子设备的硬件标识符（Hardware ID）。 |
| `uid` | ACPI 子设备的唯一标识符（Unique ID）。如果平台上只有一个具有给定 HID 的设备，`uid` 可为 `NULL`。 |

**返回（Returns）**：返回值（Returns）：成功时为 ACPI 子设备信息，否则为 `NULL`。

<a id="ab8a0982a3acc857ea059bb617b8b43f7"></a>

### `acpi_device_irq_get()`

```c
int acpi_device_irq_get ( struct acpi_dev * child_dev, struct acpi_irq_resource * irq_res )
```

解析资源表以获得中断请求（IRQ）信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `child_dev` | ACPI 节点的设备对象（Device Object）。 |
| `irq_res` | 中断请求资源信息（IRQ Resource Info）。 |

**返回（Returns）**：返回值（Returns）：成功时返回 0，否则返回错误码。

<a id="a4179d931233431ec61b5e12c1c77931d"></a>

### `acpi_device_mmio_get()`

```c
int acpi_device_mmio_get ( struct acpi_dev * child_dev, struct acpi_mmio_resource * mmio_res )
```

解析资源表以获得内存映射 I/O（MMIO）信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `child_dev` | ACPI 节点的设备对象（Device Object）。 |
| `mmio_res` | 内存映射 I/O 资源信息（MMIO Resource Info）。 |

**返回（Returns）**：返回值（Returns）：成功时返回 0，否则返回错误码。

<a id="a44b747b1b7493627a8022c49571b04ff"></a>

### `acpi_device_type_get()`

```c
int acpi_device_type_get ( ACPI_RESOURCE * res)
```

解析资源表以识别资源类型（Resource Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `res` | ACPI 资源列表（Resource List）。 |

**返回（Returns）**：返回值（Returns）：成功时为资源类型（Resource Type），否则为无效资源类型。

<a id="a36d899259fe64aea46549e54ebbfbf0a"></a>

### `acpi_dmar_entry_get()`

```c
int acpi_dmar_entry_get ( enum AcpiDmarType type, ACPI_SUBTABLE_HEADER ** tables )
```

获取给定类型的 DMA 重映射结构（DMA Remapping Structure）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `type` | 重映射结构类型（Remapping Structure Type）。 |
| `tables` | 指向 `dmar` 标识结构（ID Structure）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时返回 0，否则返回错误码。

<a id="a77d02fbe12ff3e02368582c489f7c7d5"></a>

### `acpi_dmar_foreach_devscope()`

```c
void acpi_dmar_foreach_devscope ( ACPI_DMAR_HARDWARE_UNIT * hu, dmar_foreach_devscope_func_t func, void * arg )
```

<a id="af62e15025d3442b2db39b34c3e138671"></a>

### `acpi_dmar_foreach_subtable()`

```c
void acpi_dmar_foreach_subtable ( ACPI_TABLE_DMAR * dmar, dmar_foreach_subtable_func_t func, void * arg )
```

<a id="a9768a4b3d13edb8456736256ec015e04"></a>

### `acpi_dmar_ioapic_get()`

```c
int acpi_dmar_ioapic_get ( uint16_t * ioapic_id)
```

获取 I/O 高级可编程中断控制器标识符（IOAPIC ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ioapic_id` | I/O 高级可编程中断控制器标识符（IOAPIC ID）。 |

**返回（Returns）**：返回值（Returns）：成功时返回 0，否则返回错误码。

<a id="a1d9f2e00bbcc8a0e101091c6d6be4ac5"></a>

### `acpi_drhd_get()`

```c
int acpi_drhd_get ( enum AcpiDmarScopeType scope, ACPI_DMAR_DEVICE_SCOPE * dev_scope, union acpi_dmar_id * dmar_id, int * num_inst, int max_inst )
```

获取给定作用域（Scope）的 ACPI DMA 重映射硬件单元定义（DRHD）信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `scope` | 所请求 DHRD 表的作用域（Scope；原文写作 DHRD）。 |
| `dev_scope` | 指向子表（Subtable）的指针，可选。 |
| `dmar_id` | 指向 DHRD 信息的指针（原文写作 DHRD）。 |
| `num_inst` | 所请求表的实例数量（Number of Instances）。 |
| `max_inst` | 给定 `dmar_id` 缓冲区的最大条目数。 |

**返回（Returns）**：返回值（Returns）：成功时返回 0，否则返回错误码。

<a id="aab272d92004e687bdd2936f648f3f9f9"></a>

### `acpi_invoke_method()`

```c
int acpi_invoke_method ( char * path, ACPI_OBJECT_LIST * arg_list, ACPI_OBJECT * ret_obj )
```

调用 ACPI 方法（Method）并返回结果。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | ACPI 对象的路径名（Path Name）。 |
| `arg_list` | 要向下传递的参数列表（Argument List）。 |
| `ret_obj` | 要返回的 ACPI 结果（Result）。 |

**返回（Returns）**：返回值（Returns）：成功时返回 0，否则返回错误码。

<a id="a3a0c7a6232c1f1f08ae0be3e5c3fac7a"></a>

### `acpi_irq_res_get()`

```c
ACPI_RESOURCE_IRQ * acpi_irq_res_get ( ACPI_RESOURCE * res_lst)
```

声明属性：`inline`、`static`。

解析资源表以获得中断请求（IRQ）信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `res_lst` | ACPI 资源列表（Resource List）。 |

**返回（Returns）**：返回值（Returns）：成功时为 IRQ 资源列表，否则为 `NULL`。

<a id="a139f52f8431a00d34abae1d5a5f31d92"></a>

### `acpi_legacy_irq_get()`

```c
uint32_t acpi_legacy_irq_get ( pcie_bdf_t bdf)
```

获取 PCI 设备的传统中断号（Legacy Interrupt Number）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | 端点／PCI 设备的总线、设备、功能号（Bus/Device/Function，BDF）。 |

**返回（Returns）**：返回值（Returns）：返回 IRQ 编号；未找到时返回 `UINT_MAX`。

<a id="ac97acaf39d481f3c3915c763e7f2cdc3"></a>

### `acpi_legacy_irq_init()`

```c
int acpi_legacy_irq_init ( const char * hid, const char * uid )
```

从 ACPI 初始化传统中断路由表（Legacy Interrupt Routing Table）信息。

目前假定平台只有一条 PCI 总线。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hid` | ACPI 子设备的硬件标识符（Hardware ID）。 |
| `uid` | ACPI 子设备的唯一标识符（Unique ID）。如果平台上只有一个具有给定 `hid` 的设备，`uid` 可为 `NULL`。 |

**返回（Returns）**：返回值（Returns）：成功时返回 0，否则返回错误码。

<a id="a750b6348bfc9f3867b561ff9d7a08b4c"></a>

### `acpi_local_apic_get()`

```c
ACPI_MADT_LOCAL_APIC * acpi_local_apic_get ( int cpu_num)
```

获取第 `n` 个已启用的本地高级可编程中断控制器（Local APIC）信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cpu_num` | CPU 编号（CPU Number）。 |

**返回（Returns）**：返回值（Returns）：成功时为本地 APIC 信息，否则为 `NULL`。

<a id="a379137f6a7b2a62e952dd961d0b5ed25"></a>

### `acpi_local_x2apic_get()`

```c
ACPI_MADT_LOCAL_X2APIC * acpi_local_x2apic_get ( int cpu_num)
```

获取第 `n` 个已启用的本地 x2APIC 信息（MADT 类型 9）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cpu_num` | CPU 编号（CPU Number）。 |

**返回（Returns）**：返回值（Returns）：成功时为本地 x2APIC 信息，否则为 `NULL`。

<a id="abb83809ce252f82f93ea042dfba3fbfd"></a>

### `acpi_madt_entry_get()`

```c
int acpi_madt_entry_get ( int type, ACPI_SUBTABLE_HEADER ** tables, int * num_inst )
```

获取给定类型的 ACPI MAD 表（MAD Table）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `type` | 所请求 MAD 表的类型（Type）。 |
| `tables` | 指向 MAD 表的指针。 |
| `num_inst` | 所请求表的实例数量（Number of Instances）。 |

**返回（Returns）**：返回值（Returns）：成功时返回 0，否则返回错误码。

<a id="a5787a05051ffb4ccab113cf2e834678d"></a>

### `acpi_possible_resource_get()`

```c
int acpi_possible_resource_get ( char * dev_name, ACPI_RESOURCE ** res )
```

获取设备可能的资源设置（Possible Resource Settings）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev_name` | 设备名称（Device Name）。 |
| `res` | ACPI 资源列表（Resource List）。 |

**返回（Returns）**：返回值（Returns）：成功时返回 0，否则返回错误码。

<a id="afaad7277ab95c5d5cbf2d66407cdc7fa"></a>

### `acpi_poweroff()`

```c
int acpi_poweroff ( void )
```

将系统设为软关机（Soft Off）状态，以执行系统级关机。

要求启用 `CONFIG_ACPI_POWEROFF`。

**返回（Returns）**：返回值（Returns）：`pm1_cnt` 地址不可用时为 `-EINVAL`。

<a id="aa5d7b0c25e6e2767c15edbce33971c72"></a>

### `acpi_resource_parse()`

```c
ACPI_RESOURCE * acpi_resource_parse ( ACPI_RESOURCE * res, int res_type )
```

按给定资源类型（Resource Type）解析资源表。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `res` | ACPI 资源列表（Resource List）。 |
| `res_type` | ACPI 资源类型（Resource Type）。 |

**返回（Returns）**：返回值（Returns）：成功时为给定类型的资源列表，否则为 `NULL`。

<a id="ab6f0b5f0ae6cf1da923051f2e38fa193"></a>

### `acpi_table_get()`

```c
void * acpi_table_get ( char * signature, int inst )
```

获取与给定签名（Signature）对应的 ACPI 表。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `signature` | 指向所请求表的 4 字符 ACPI 签名（Signature）的指针。 |
| `inst` | 所请求表的实例编号（Instance Number）。 |

**返回（Returns）**：返回值（Returns）：成功时为指向 ACPI 表的 `acpi_table` 指针，否则为 `NULL`。


## 2.7\_原页交叉引用（Cross References）

- [zephyr/drivers/pcie/pcie.h](../api_source_pcie_hid_reference/P001_pcie.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P003_acpi.h_源码浏览.md)
- [acpi_dev](../driver_model_reference/P001_ACPI设备.md)
- [acpi_dmar_id](../platform_security_model_reference/P076_acpi_dmar_id_联合体.md)
- [acpi_mcfg](../driver_model_reference/P003_ACPI内存配置表.md)
- [acpi_irq_resource](../driver_model_reference/P002_ACPI中断资源.md)
- [acpi_reg_base](../driver_model_reference/P005_ACPI寄存器基址.md)
- [acpi_mmio_resource](../driver_model_reference/P004_ACPI内存映射资源.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [pcie_bdf_t](../api_memory_timer_topic_reference/P008_PCIe 主机（PCIe Host）.md#gaf9748042a4f3c8d912d19df1ccf737fb)
- [child_dev](../api_buffer_paging_topic_reference/P012_MFD ADP5360 接口.md#gae4d56fd30130dc4f332ecf43465a1558)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [DT_NODE_HAS_PROP](../dt_identity_reference/P002_设备树存在性与状态宏.md#gacce67bf20541cd2d07d8540058964692)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)
- [DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)
- [CONFIG_ACPI_POWEROFF](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ACPI_POWEROFF)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-exist_html_gacce67bf20541cd2d07d8540058964692"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>
<a id="agroup__devicetree-generic-prop_html_ga5e5bfc9b1a6627b3f73014329e96340f"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a225bfac5f9770bd826ae98d2bbbbfc5badde21e335fe3363fd60eb3076dfe7a9f"></a>
<a id="a225bfac5f9770bd826ae98d2bbbbfc5ba609d72a263b7ed46da533aeab6255626"></a>
<a id="a225bfac5f9770bd826ae98d2bbbbfc5bad9f5eaef7ee5ef391c917786a358278b"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_zephyr__bluetooth__mesh__access.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__bluetooth__audio__audio.h_文件参考.md)
