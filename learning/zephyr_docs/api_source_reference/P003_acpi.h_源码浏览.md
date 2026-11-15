---
id: learning.zephyr-docs.api-source-reference.page-3
title: acpi.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_acpi.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html)。

## 3.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00057"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="foldopen00069"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="foldopen00078"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="foldopen00194"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="aacpi_2acpi_8h_html_a139f52f8431a00d34abae1d5a5f31d92"></a>
<a id="aacpi_2acpi_8h_html_a1d9f2e00bbcc8a0e101091c6d6be4ac5"></a>
<a id="aacpi_2acpi_8h_html_a225bfac5f9770bd826ae98d2bbbbfc5b"></a>
<a id="aacpi_2acpi_8h_html_a225bfac5f9770bd826ae98d2bbbbfc5ba609d72a263b7ed46da533aeab6255626"></a>
<a id="aacpi_2acpi_8h_html_a225bfac5f9770bd826ae98d2bbbbfc5bad9f5eaef7ee5ef391c917786a358278b"></a>
<a id="aacpi_2acpi_8h_html_a225bfac5f9770bd826ae98d2bbbbfc5badde21e335fe3363fd60eb3076dfe7a9f"></a>
<a id="aacpi_2acpi_8h_html_a36d899259fe64aea46549e54ebbfbf0a"></a>
<a id="aacpi_2acpi_8h_html_a379137f6a7b2a62e952dd961d0b5ed25"></a>
<a id="aacpi_2acpi_8h_html_a3a0c7a6232c1f1f08ae0be3e5c3fac7a"></a>
<a id="aacpi_2acpi_8h_html_a4179d931233431ec61b5e12c1c77931d"></a>
<a id="aacpi_2acpi_8h_html_a44b747b1b7493627a8022c49571b04ff"></a>
<a id="aacpi_2acpi_8h_html_a5787a05051ffb4ccab113cf2e834678d"></a>
<a id="aacpi_2acpi_8h_html_a625d35bab5922b679517fe8d8b0aface"></a>
<a id="aacpi_2acpi_8h_html_a6416a93af8385d3784d205b8811a6a94"></a>
<a id="aacpi_2acpi_8h_html_a6b294403ca4a5e1c234c42279d201490"></a>
<a id="aacpi_2acpi_8h_html_a703f435a640e34080a6cf52c2256294e"></a>
<a id="aacpi_2acpi_8h_html_a750b6348bfc9f3867b561ff9d7a08b4c"></a>
<a id="aacpi_2acpi_8h_html_a77d02fbe12ff3e02368582c489f7c7d5"></a>
<a id="aacpi_2acpi_8h_html_a9768a4b3d13edb8456736256ec015e04"></a>
<a id="aacpi_2acpi_8h_html_aa5d7b0c25e6e2767c15edbce33971c72"></a>
<a id="aacpi_2acpi_8h_html_aab272d92004e687bdd2936f648f3f9f9"></a>
<a id="aacpi_2acpi_8h_html_ab6f0b5f0ae6cf1da923051f2e38fa193"></a>
<a id="aacpi_2acpi_8h_html_ab8a0982a3acc857ea059bb617b8b43f7"></a>
<a id="aacpi_2acpi_8h_html_abb83809ce252f82f93ea042dfba3fbfd"></a>
<a id="aacpi_2acpi_8h_html_ac97acaf39d481f3c3915c763e7f2cdc3"></a>
<a id="aacpi_2acpi_8h_html_ae8d0e92bc9f94d1c70dc893b686c29de"></a>
<a id="aacpi_2acpi_8h_html_af62e15025d3442b2db39b34c3e138671"></a>
<a id="aacpi_2acpi_8h_html_af675794f8aa74fb58c7a2c7266f05357"></a>
<a id="aacpi_2acpi_8h_html_afaad7277ab95c5d5cbf2d66407cdc7fa"></a>
<a id="adrivers_2pcie_2pcie_8h_html"></a>
<a id="agroup__mfd__interface__adp5360_html_gae4d56fd30130dc4f332ecf43465a1558"></a>
<a id="agroup__pcie__host__interface_html_gaf9748042a4f3c8d912d19df1ccf737fb"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructacpi__dev_html"></a>
<a id="astructacpi__dev_html_a181c2fdd63f316b1d69f3cdc0d924fe2"></a>
<a id="astructacpi__dev_html_a521452067b5751a2a59d156b13ff24f1"></a>
<a id="astructacpi__dev_html_a54c5c7c33a425b565b0e1337063a1c1a"></a>
<a id="astructacpi__dev_html_abc282bce7cdc3de32feb57bc4da790e8"></a>
<a id="astructacpi__dev_html_ace9e72f625889d0f84caa17ee6dc8e24"></a>
<a id="astructacpi__irq__resource_html"></a>
<a id="astructacpi__irq__resource_html_a261bdfee8d5a1137a30bd498e1c5b3c4"></a>
<a id="astructacpi__irq__resource_html_a8d5d5ddb21f52e432862cd0fb16f5f0a"></a>
<a id="astructacpi__irq__resource_html_ac79f9ccd199de7fa52208dee857e7e8f"></a>
<a id="astructacpi__mcfg_html"></a>
<a id="astructacpi__mcfg_html_a8d6bc322dcb14c2892382067275f2426"></a>
<a id="astructacpi__mcfg_html_ac3745fb726a32a57992556b9dbaa1365"></a>
<a id="astructacpi__mmio__resource_html"></a>
<a id="astructacpi__mmio__resource_html_a26d31589732a487adbe7b2ab862c4ff4"></a>
<a id="astructacpi__mmio__resource_html_ae4ab8715b8f13fa57bc983393c8bd5e6"></a>
<a id="astructacpi__reg__base_html"></a>
<a id="astructacpi__reg__base_html_a416f2ff166b33add65eba5e7787c3ef5"></a>
<a id="astructacpi__reg__base_html_aaca25908e4e16a71627c48208c55d0ef"></a>
<a id="astructacpi__reg__base_html_ab845df09e3b4b9734103605ea7c65d1e"></a>
<a id="astructacpi__reg__base_html_ada6ffb943e406068271d56b5a129b717"></a>
<a id="aunionacpi__dmar__id_html"></a>
<a id="aunionacpi__dmar__id_html_a03e48f74dae90bbbeba96c4d9f274020"></a>
<a id="aunionacpi__dmar__id_html_a0fffa1ca831591b42f732acfd1d86aa6"></a>
<a id="aunionacpi__dmar__id_html_a3e9194555004762db83d9853594ffca1"></a>
<a id="aunionacpi__dmar__id_html_a700729e862c40298e4ebe05b7881f009"></a>
<a id="aunionacpi__dmar__id_html_a8fe219b9f4f5871cf14d01079af79614"></a>

```c
/*
 * Copyright (c) 2023 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_ACPI_ACPI_H_
#define ZEPHYR_INCLUDE_ACPI_ACPI_H_
#include <acpica/source/include/acpi.h>
#include <zephyr/drivers/pcie/pcie.h>

#define ACPI_RES_INVALID ACPI_RESOURCE_TYPE_MAX

#define ACPI_DRHD_FLAG_INCLUDE_PCI_ALL                  BIT(0)
#define ACPI_DMAR_FLAG_INTR_REMAP                               BIT(0)
#define ACPI_DMAR_FLAG_X2APIC_OPT_OUT                   BIT(1)
#define ACPI_DMAR_FLAG_DMA_CTRL_PLATFORM_OPT_IN BIT(2)

#define ACPI_MMIO_GET(res) (res)->reg_base[0].mmio
#define ACPI_IO_GET(res) (res)->reg_base[0].port
#define ACPI_RESOURCE_SIZE_GET(res) (res)->reg_base[0].length
#define ACPI_RESOURCE_TYPE_GET(res) (res)->reg_base[0].type

#define ACPI_MULTI_MMIO_GET(res, idx) (res)->reg_base[idx].mmio
#define ACPI_MULTI_IO_GET(res, idx) (res)->reg_base[idx].port
#define ACPI_MULTI_RESOURCE_SIZE_GET(res, idx) (res)->reg_base[idx].length
#define ACPI_MULTI_RESOURCE_TYPE_GET(res, idx) (res)->reg_base[idx].type

#define ACPI_RESOURCE_COUNT_GET(res) (res)->mmio_max

enum acpi_res_type {
        ACPI_RES_TYPE_IO,
        ACPI_RES_TYPE_MEM,
        ACPI_RES_TYPE_UNKNOWN,
};

struct acpi_dev {
        ACPI_HANDLE handle;
        char *path;
        ACPI_RESOURCE *res_lst;
        int res_type;
        ACPI_DEVICE_INFO *dev_info;
};

union acpi_dmar_id {
        struct {
                uint16_t function: 3;
                uint16_t device: 5;
                uint16_t bus: 8;
        } bits;

        uint16_t raw;
};

struct acpi_mcfg {
        ACPI_TABLE_HEADER header;
        uint64_t _reserved;
        ACPI_MCFG_ALLOCATION pci_segs[];
} __packed;

struct acpi_irq_resource {
        uint32_t flags;
        uint8_t irq_vector_max;
        uint16_t *irqs;
};

struct acpi_reg_base {
        enum acpi_res_type type;
        union {
                uintptr_t mmio;
                uintptr_t port;
        };
        uint32_t length;
};

struct acpi_mmio_resource {
        uint8_t mmio_max;
        struct acpi_reg_base *reg_base;
};

#define ACPI_DT_HID(node_id) DT_PROP(node_id, acpi_hid)

#define ACPI_DT_UID(node_id) DT_PROP_OR(node_id, acpi_uid, NULL)

#define ACPI_DT_HAS_HID(node_id) DT_NODE_HAS_PROP(node_id, acpi_hid)

#define ACPI_DT_HAS_UID(node_id) DT_NODE_HAS_PROP(node_id, acpi_uid)

int acpi_legacy_irq_init(const char *hid, const char *uid);

uint32_t acpi_legacy_irq_get(pcie_bdf_t bdf);

int acpi_current_resource_get(char *dev_name, ACPI_RESOURCE **res);

int acpi_possible_resource_get(char *dev_name, ACPI_RESOURCE **res);

int acpi_current_resource_free(ACPI_RESOURCE *res);

ACPI_RESOURCE *acpi_resource_parse(ACPI_RESOURCE *res, int res_type);

struct acpi_dev *acpi_device_get(const char *hid, const char *uid);

struct acpi_dev *acpi_device_by_index_get(int index);

static inline ACPI_RESOURCE_IRQ *acpi_irq_res_get(ACPI_RESOURCE *res_lst)
{
        ACPI_RESOURCE *res = acpi_resource_parse(res_lst, ACPI_RESOURCE_TYPE_IRQ);

        return res ? &res->Data.Irq : NULL;
}

int acpi_device_irq_get(struct acpi_dev *child_dev, struct acpi_irq_resource *irq_res);

int acpi_device_mmio_get(struct acpi_dev *child_dev, struct acpi_mmio_resource *mmio_res);

int acpi_device_type_get(ACPI_RESOURCE *res);

void *acpi_table_get(char *signature, int inst);

int acpi_madt_entry_get(int type, ACPI_SUBTABLE_HEADER **tables, int *num_inst);

int acpi_dmar_entry_get(enum AcpiDmarType type, ACPI_SUBTABLE_HEADER **tables);

int acpi_drhd_get(enum AcpiDmarScopeType scope, ACPI_DMAR_DEVICE_SCOPE *dev_scope,
                  union acpi_dmar_id *dmar_id, int *num_inst, int max_inst);

typedef void (*dmar_foreach_subtable_func_t)(ACPI_DMAR_HEADER *subtable, void *arg);
typedef void (*dmar_foreach_devscope_func_t)(ACPI_DMAR_DEVICE_SCOPE *devscope, void *arg);

void acpi_dmar_foreach_subtable(ACPI_TABLE_DMAR *dmar, dmar_foreach_subtable_func_t func,
                                void *arg);
void acpi_dmar_foreach_devscope(ACPI_DMAR_HARDWARE_UNIT *hu,
                                dmar_foreach_devscope_func_t func, void *arg);

int acpi_dmar_ioapic_get(uint16_t *ioapic_id);

ACPI_MADT_LOCAL_APIC *acpi_local_apic_get(int cpu_num);

ACPI_MADT_LOCAL_X2APIC *acpi_local_x2apic_get(int cpu_num);

int acpi_invoke_method(char *path, ACPI_OBJECT_LIST *arg_list, ACPI_OBJECT *ret_obj);

#if defined(CONFIG_ACPI_POWEROFF) || defined(__DOXYGEN__)
int acpi_poweroff(void);
#else
static inline int acpi_poweroff(void)
{
        return -ENOTSUP;
}
#endif /* CONFIG_ACPI_POWEROFF */

#endif /* ZEPHYR_INCLUDE_ACPI_ACPI_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 323 行

条件编译配置（Configuration）标记：`CONFIG_ACPI_POWEROFF`。

### 注释 3：原第 325 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ACPI_ACPI_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html)
- [zephyr/drivers/pcie/pcie.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2pcie_8h.html)
- [acpi_res_type](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a225bfac5f9770bd826ae98d2bbbbfc5b)
- [ACPI_RES_TYPE_IO](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a225bfac5f9770bd826ae98d2bbbbfc5badde21e335fe3363fd60eb3076dfe7a9f)
- [ACPI_RES_TYPE_MEM](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a225bfac5f9770bd826ae98d2bbbbfc5ba609d72a263b7ed46da533aeab6255626)
- [ACPI_RES_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a225bfac5f9770bd826ae98d2bbbbfc5bad9f5eaef7ee5ef391c917786a358278b)
- [acpi_dev](../driver_model_reference/P001_ACPI设备.md)
- [handle](../driver_model_reference/P001_ACPI设备.md#ace9e72f625889d0f84caa17ee6dc8e24)
- [path](../driver_model_reference/P001_ACPI设备.md#a181c2fdd63f316b1d69f3cdc0d924fe2)
- [res_lst](../driver_model_reference/P001_ACPI设备.md#a54c5c7c33a425b565b0e1337063a1c1a)
- [res_type](../driver_model_reference/P001_ACPI设备.md#abc282bce7cdc3de32feb57bc4da790e8)
- [dev_info](../driver_model_reference/P001_ACPI设备.md#a521452067b5751a2a59d156b13ff24f1)
- [acpi_dmar_id](../platform_security_model_reference/P076_acpi_dmar_id_联合体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [function](../platform_security_model_reference/P076_acpi_dmar_id_联合体.md#a8fe219b9f4f5871cf14d01079af79614)
- [device](../platform_security_model_reference/P076_acpi_dmar_id_联合体.md#a03e48f74dae90bbbeba96c4d9f274020)
- [bus](../platform_security_model_reference/P076_acpi_dmar_id_联合体.md#a3e9194555004762db83d9853594ffca1)
- [bits](../platform_security_model_reference/P076_acpi_dmar_id_联合体.md#a0fffa1ca831591b42f732acfd1d86aa6)
- [raw](../platform_security_model_reference/P076_acpi_dmar_id_联合体.md#a700729e862c40298e4ebe05b7881f009)
- [acpi_mcfg](../driver_model_reference/P003_ACPI内存配置表.md)
- [header](../driver_model_reference/P003_ACPI内存配置表.md#ac3745fb726a32a57992556b9dbaa1365)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [pci_segs](../driver_model_reference/P003_ACPI内存配置表.md#a8d6bc322dcb14c2892382067275f2426)
- [acpi_irq_resource](../driver_model_reference/P002_ACPI中断资源.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flags](../driver_model_reference/P002_ACPI中断资源.md#ac79f9ccd199de7fa52208dee857e7e8f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [irq_vector_max](../driver_model_reference/P002_ACPI中断资源.md#a8d5d5ddb21f52e432862cd0fb16f5f0a)
- [irqs](../driver_model_reference/P002_ACPI中断资源.md#a261bdfee8d5a1137a30bd498e1c5b3c4)
- [acpi_reg_base](../driver_model_reference/P005_ACPI寄存器基址.md)
- [type](../driver_model_reference/P005_ACPI寄存器基址.md#a416f2ff166b33add65eba5e7787c3ef5)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [mmio](../driver_model_reference/P005_ACPI寄存器基址.md#ada6ffb943e406068271d56b5a129b717)
- [port](../driver_model_reference/P005_ACPI寄存器基址.md#ab845df09e3b4b9734103605ea7c65d1e)
- [length](../driver_model_reference/P005_ACPI寄存器基址.md#aaca25908e4e16a71627c48208c55d0ef)
- [acpi_mmio_resource](../driver_model_reference/P004_ACPI内存映射资源.md)
- [mmio_max](../driver_model_reference/P004_ACPI内存映射资源.md#a26d31589732a487adbe7b2ab862c4ff4)
- [reg_base](../driver_model_reference/P004_ACPI内存映射资源.md#ae4ab8715b8f13fa57bc983393c8bd5e6)
- [acpi_legacy_irq_init](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#ac97acaf39d481f3c3915c763e7f2cdc3)
- [acpi_legacy_irq_get](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a139f52f8431a00d34abae1d5a5f31d92)
- [pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)
- [acpi_current_resource_get](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#ae8d0e92bc9f94d1c70dc893b686c29de)
- [acpi_possible_resource_get](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a5787a05051ffb4ccab113cf2e834678d)
- [acpi_current_resource_free](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a703f435a640e34080a6cf52c2256294e)
- [acpi_resource_parse](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#aa5d7b0c25e6e2767c15edbce33971c72)
- [acpi_device_get](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a6416a93af8385d3784d205b8811a6a94)
- [acpi_device_by_index_get](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a625d35bab5922b679517fe8d8b0aface)
- [acpi_irq_res_get](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a3a0c7a6232c1f1f08ae0be3e5c3fac7a)
- [acpi_device_irq_get](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#ab8a0982a3acc857ea059bb617b8b43f7)
- [child_dev](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gae4d56fd30130dc4f332ecf43465a1558)
- [acpi_device_mmio_get](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a4179d931233431ec61b5e12c1c77931d)
- [acpi_device_type_get](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a44b747b1b7493627a8022c49571b04ff)
- [acpi_table_get](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#ab6f0b5f0ae6cf1da923051f2e38fa193)
- [acpi_madt_entry_get](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#abb83809ce252f82f93ea042dfba3fbfd)
- [acpi_dmar_entry_get](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a36d899259fe64aea46549e54ebbfbf0a)
- [acpi_drhd_get](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a1d9f2e00bbcc8a0e101091c6d6be4ac5)
- [dmar_foreach_subtable_func_t](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#af675794f8aa74fb58c7a2c7266f05357)
- [dmar_foreach_devscope_func_t](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a6b294403ca4a5e1c234c42279d201490)
- [acpi_dmar_foreach_subtable](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#af62e15025d3442b2db39b34c3e138671)
- [acpi_dmar_foreach_devscope](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a77d02fbe12ff3e02368582c489f7c7d5)
- [acpi_dmar_ioapic_get](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a9768a4b3d13edb8456736256ec015e04)
- [acpi_local_apic_get](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a750b6348bfc9f3867b561ff9d7a08b4c)
- [acpi_local_x2apic_get](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a379137f6a7b2a62e952dd961d0b5ed25)
- [acpi_invoke_method](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#aab272d92004e687bdd2936f648f3f9f9)
- [acpi_poweroff](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#afaad7277ab95c5d5cbf2d66407cdc7fa)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [pcie.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2pcie_8h.html)
- [acpi_dev::path](../driver_model_reference/P001_ACPI设备.md#a181c2fdd63f316b1d69f3cdc0d924fe2)
- [acpi_dev::dev_info](../driver_model_reference/P001_ACPI设备.md#a521452067b5751a2a59d156b13ff24f1)
- [acpi_dev::res_lst](../driver_model_reference/P001_ACPI设备.md#a54c5c7c33a425b565b0e1337063a1c1a)
- [acpi_dev::res_type](../driver_model_reference/P001_ACPI设备.md#abc282bce7cdc3de32feb57bc4da790e8)
- [acpi_dev::handle](../driver_model_reference/P001_ACPI设备.md#ace9e72f625889d0f84caa17ee6dc8e24)
- [acpi_irq_resource::irqs](../driver_model_reference/P002_ACPI中断资源.md#a261bdfee8d5a1137a30bd498e1c5b3c4)
- [acpi_irq_resource::irq_vector_max](../driver_model_reference/P002_ACPI中断资源.md#a8d5d5ddb21f52e432862cd0fb16f5f0a)
- [acpi_irq_resource::flags](../driver_model_reference/P002_ACPI中断资源.md#ac79f9ccd199de7fa52208dee857e7e8f)
- [acpi_mcfg::pci_segs](../driver_model_reference/P003_ACPI内存配置表.md#a8d6bc322dcb14c2892382067275f2426)
- [acpi_mcfg::header](../driver_model_reference/P003_ACPI内存配置表.md#ac3745fb726a32a57992556b9dbaa1365)
- [acpi_mmio_resource::mmio_max](../driver_model_reference/P004_ACPI内存映射资源.md#a26d31589732a487adbe7b2ab862c4ff4)
- [acpi_mmio_resource::reg_base](../driver_model_reference/P004_ACPI内存映射资源.md#ae4ab8715b8f13fa57bc983393c8bd5e6)
- [acpi_reg_base::type](../driver_model_reference/P005_ACPI寄存器基址.md#a416f2ff166b33add65eba5e7787c3ef5)
- [acpi_reg_base::length](../driver_model_reference/P005_ACPI寄存器基址.md#aaca25908e4e16a71627c48208c55d0ef)
- [acpi_reg_base::port](../driver_model_reference/P005_ACPI寄存器基址.md#ab845df09e3b4b9734103605ea7c65d1e)
- [acpi_reg_base::mmio](../driver_model_reference/P005_ACPI寄存器基址.md#ada6ffb943e406068271d56b5a129b717)
- [acpi_dmar_id::device](../platform_security_model_reference/P076_acpi_dmar_id_联合体.md#a03e48f74dae90bbbeba96c4d9f274020)
- [acpi_dmar_id::bits](../platform_security_model_reference/P076_acpi_dmar_id_联合体.md#a0fffa1ca831591b42f732acfd1d86aa6)
- [acpi_dmar_id::bus](../platform_security_model_reference/P076_acpi_dmar_id_联合体.md#a3e9194555004762db83d9853594ffca1)
- [acpi_dmar_id::raw](../platform_security_model_reference/P076_acpi_dmar_id_联合体.md#a700729e862c40298e4ebe05b7881f009)
- [acpi_dmar_id::function](../platform_security_model_reference/P076_acpi_dmar_id_联合体.md#a8fe219b9f4f5871cf14d01079af79614)

---

[上一章](P002_ac057tc1.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P004_acpi_osal.h_源码浏览.md)
