---
id: learning.zephyr-docs.api-source-supplement-reference.page-238
title: usbc_ppc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbc__ppc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第238章\_usbc\_ppc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usbc__ppc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/usbc__ppc_8h.html)。

## 238.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00074"></a>
<a id="foldopen00078"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="foldopen00116"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="foldopen00139"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="foldopen00159"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="foldopen00179"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="foldopen00199"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="foldopen00219"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="foldopen00239"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="foldopen00259"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="foldopen00279"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="foldopen00299"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="agroup__usb__type__c__power__path__controller_html_ga1d59cc94e8d303f0125fc88e5b447a69"></a>
<a id="agroup__usb__type__c__power__path__controller_html_ga3dbbb1a6701a3a79c9a1d148b239fcf9"></a>
<a id="agroup__usb__type__c__power__path__controller_html_ga5f70af9a0d0336c208ff4f7a90c4b665"></a>
<a id="agroup__usb__type__c__power__path__controller_html_ga8195a7a51eb5bd3cbcec985b97b84e73"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gaab85fda6d4030c83052deb1965d814f3"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gabcbebdf47ca1c8a9b7c2e803bb833f5a"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gacd1ac1ac4ea60f16c58f57c9df11d536"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gad38e1b5b5598c23ded44b343af58b791"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gae157ab53326686361309f20dfe5c4e64"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gae66cb0377ffefabf85bc002a2fd04a47"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gaeee650c29ce524b1e4d8ef66f295c1d7"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gaf5e3999f3a016e33adf4797b62009d6d"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gga3dbbb1a6701a3a79c9a1d148b239fcf9a3eca3adb253db52fb444c0163781dde6"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gga3dbbb1a6701a3a79c9a1d148b239fcf9a4fbd9543f2596349d26d7c1cc6278238"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gga3dbbb1a6701a3a79c9a1d148b239fcf9a54615a71ead7913f6eb708be78fee109"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gga3dbbb1a6701a3a79c9a1d148b239fcf9a6d189e6a1c326f6746cb3e4abd0a7759"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gga3dbbb1a6701a3a79c9a1d148b239fcf9a7e6392785fe1d6f5c3cef3b179952b0e"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gga3dbbb1a6701a3a79c9a1d148b239fcf9a8e6635e7e347418f328ce5ebcb303d5e"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gga3dbbb1a6701a3a79c9a1d148b239fcf9aa4434d091f55ad29e7fb46b681fc376d"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gga3dbbb1a6701a3a79c9a1d148b239fcf9aaa39462464dfaf5a0f57fa6407114b94"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gga3dbbb1a6701a3a79c9a1d148b239fcf9ac241608a878e709571144ad5f207140c"></a>
<a id="agroup__usb__type__c__power__path__controller_html_gga3dbbb1a6701a3a79c9a1d148b239fcf9addcec15b50f34307780822cb1fc329c4"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructusbc__ppc__driver__api_html"></a>
<a id="astructusbc__ppc__driver__api_html_a1c2c21070ee18b7b5df09a6b6ed618b6"></a>
<a id="astructusbc__ppc__driver__api_html_a20ddefaee68808414f4075cc513a8660"></a>
<a id="astructusbc__ppc__driver__api_html_a4ba2f654765130d5562f56243967bf58"></a>
<a id="astructusbc__ppc__driver__api_html_a832320573b2adab1d748e5e761690733"></a>
<a id="astructusbc__ppc__driver__api_html_a8bf73dee9ba920f1b426038f62d5c9db"></a>
<a id="astructusbc__ppc__driver__api_html_a8f82ae3af5452d9cd0852bf15fcab573"></a>
<a id="astructusbc__ppc__driver__api_html_a93b91d21d4d2edda1d457f4144800f37"></a>
<a id="astructusbc__ppc__driver__api_html_aab74a38a9c055efdfd0198143f12c9ff"></a>
<a id="astructusbc__ppc__driver__api_html_adce51ae345d5fc417f3767476af36276"></a>
<a id="astructusbc__ppc__driver__api_html_af4a66a11b66d48818123434c59553f0d"></a>

```c
/*
 * Copyright 2023 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_PPC_H_
#define ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_PPC_H_


#include <zephyr/types.h>
#include <zephyr/device.h>
#include <errno.h>

#ifdef __cplusplus
extern "C" {
#endif

enum usbc_ppc_event {
        USBC_PPC_EVENT_DEAD_BATTERY_ERROR = 0,

        USBC_PPC_EVENT_SRC_OVERVOLTAGE,
        USBC_PPC_EVENT_SRC_REVERSE_CURRENT,
        USBC_PPC_EVENT_SRC_OVERCURRENT,
        USBC_PPC_EVENT_SRC_SHORT,

        USBC_PPC_EVENT_OVER_TEMPERATURE,
        USBC_PPC_EVENT_BOTH_SNKSRC_ENABLED,

        USBC_PPC_EVENT_SNK_REVERSE_CURRENT,
        USBC_PPC_EVENT_SNK_SHORT,
        USBC_PPC_EVENT_SNK_OVERVOLTAGE,
};

typedef void (*usbc_ppc_event_cb_t)(const struct device *dev, void *data, enum usbc_ppc_event ev);


__subsystem struct usbc_ppc_driver_api {
        int (*is_dead_battery_mode)(const struct device *dev);
        int (*exit_dead_battery_mode)(const struct device *dev);
        int (*is_vbus_source)(const struct device *dev);
        int (*is_vbus_sink)(const struct device *dev);
        int (*set_snk_ctrl)(const struct device *dev, bool enable);
        int (*set_src_ctrl)(const struct device *dev, bool enable);
        int (*set_vbus_discharge)(const struct device *dev, bool enable);
        int (*is_vbus_present)(const struct device *dev);
        int (*set_event_handler)(const struct device *dev, usbc_ppc_event_cb_t handler, void *data);
        int (*dump_regs)(const struct device *dev);
};


/*
 * API functions
 */

static inline int ppc_is_dead_battery_mode(const struct device *dev)
{
        const struct usbc_ppc_driver_api *api = DEVICE_API_GET(usbc_ppc, dev);

        if (api->is_dead_battery_mode == NULL) {
                return -ENOSYS;
        }

        return api->is_dead_battery_mode(dev);
}

static inline int ppc_exit_dead_battery_mode(const struct device *dev)
{
        const struct usbc_ppc_driver_api *api = DEVICE_API_GET(usbc_ppc, dev);

        if (api->exit_dead_battery_mode == NULL) {
                return -ENOSYS;
        }

        return api->exit_dead_battery_mode(dev);
}

static inline int ppc_is_vbus_source(const struct device *dev)
{
        const struct usbc_ppc_driver_api *api = DEVICE_API_GET(usbc_ppc, dev);

        if (api->is_vbus_source == NULL) {
                return -ENOSYS;
        }

        return api->is_vbus_source(dev);
}

static inline int ppc_is_vbus_sink(const struct device *dev)
{
        const struct usbc_ppc_driver_api *api = DEVICE_API_GET(usbc_ppc, dev);

        if (api->is_vbus_sink == NULL) {
                return -ENOSYS;
        }

        return api->is_vbus_sink(dev);
}

static inline int ppc_set_snk_ctrl(const struct device *dev, bool enable)
{
        const struct usbc_ppc_driver_api *api = DEVICE_API_GET(usbc_ppc, dev);

        if (api->set_snk_ctrl == NULL) {
                return -ENOSYS;
        }

        return api->set_snk_ctrl(dev, enable);
}

static inline int ppc_set_src_ctrl(const struct device *dev, bool enable)
{
        const struct usbc_ppc_driver_api *api = DEVICE_API_GET(usbc_ppc, dev);

        if (api->set_src_ctrl == NULL) {
                return -ENOSYS;
        }

        return api->set_src_ctrl(dev, enable);
}

static inline int ppc_set_vbus_discharge(const struct device *dev, bool enable)
{
        const struct usbc_ppc_driver_api *api = DEVICE_API_GET(usbc_ppc, dev);

        if (api->set_vbus_discharge == NULL) {
                return -ENOSYS;
        }

        return api->set_vbus_discharge(dev, enable);
}

static inline int ppc_is_vbus_present(const struct device *dev)
{
        const struct usbc_ppc_driver_api *api = DEVICE_API_GET(usbc_ppc, dev);

        if (api->is_vbus_present == NULL) {
                return -ENOSYS;
        }

        return api->is_vbus_present(dev);
}

static inline int ppc_set_event_handler(const struct device *dev,
        usbc_ppc_event_cb_t handler, void *data)
{
        const struct usbc_ppc_driver_api *api = DEVICE_API_GET(usbc_ppc, dev);

        if (api->set_event_handler == NULL) {
                return -ENOSYS;
        }

        return api->set_event_handler(dev, handler, data);
}

static inline int ppc_dump_regs(const struct device *dev)
{
        const struct usbc_ppc_driver_api *api = DEVICE_API_GET(usbc_ppc, dev);

        if (api->dump_regs == NULL) {
                return -ENOSYS;
        }

        return api->dump_regs(dev);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_PPC_H_ */
```

## 238.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 103 行

API 函数（API functions）。

### 注释 3：原第 318 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_PPC_H_`。

## 238.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/usbc__ppc_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [usbc_ppc_event](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#ga3dbbb1a6701a3a79c9a1d148b239fcf9)
- [USBC_PPC_EVENT_DEAD_BATTERY_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a8e6635e7e347418f328ce5ebcb303d5e)
- [USBC_PPC_EVENT_SRC_OVERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a54615a71ead7913f6eb708be78fee109)
- [USBC_PPC_EVENT_SRC_REVERSE_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a3eca3adb253db52fb444c0163781dde6)
- [USBC_PPC_EVENT_SRC_OVERCURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a4fbd9543f2596349d26d7c1cc6278238)
- [USBC_PPC_EVENT_SRC_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9addcec15b50f34307780822cb1fc329c4)
- [USBC_PPC_EVENT_OVER_TEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9ac241608a878e709571144ad5f207140c)
- [USBC_PPC_EVENT_BOTH_SNKSRC_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9aaa39462464dfaf5a0f57fa6407114b94)
- [USBC_PPC_EVENT_SNK_REVERSE_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a6d189e6a1c326f6746cb3e4abd0a7759)
- [USBC_PPC_EVENT_SNK_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9aa4434d091f55ad29e7fb46b681fc376d)
- [USBC_PPC_EVENT_SNK_OVERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gga3dbbb1a6701a3a79c9a1d148b239fcf9a7e6392785fe1d6f5c3cef3b179952b0e)
- [usbc_ppc_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#ga8195a7a51eb5bd3cbcec985b97b84e73)
- [device](../device_reference/P002_设备对象结构.md)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [usbc_ppc_driver_api](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md)
- [is_dead_battery_mode](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#a832320573b2adab1d748e5e761690733)
- [exit_dead_battery_mode](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#a4ba2f654765130d5562f56243967bf58)
- [is_vbus_source](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#aab74a38a9c055efdfd0198143f12c9ff)
- [is_vbus_sink](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#a93b91d21d4d2edda1d457f4144800f37)
- [set_snk_ctrl](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#af4a66a11b66d48818123434c59553f0d)
- [set_src_ctrl](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#a20ddefaee68808414f4075cc513a8660)
- [set_vbus_discharge](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#a1c2c21070ee18b7b5df09a6b6ed618b6)
- [is_vbus_present](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#a8bf73dee9ba920f1b426038f62d5c9db)
- [set_event_handler](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#a8f82ae3af5452d9cd0852bf15fcab573)
- [dump_regs](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#adce51ae345d5fc417f3767476af36276)
- [ppc_is_dead_battery_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#ga5f70af9a0d0336c208ff4f7a90c4b665)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [ppc_exit_dead_battery_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gabcbebdf47ca1c8a9b7c2e803bb833f5a)
- [ppc_is_vbus_source](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gaab85fda6d4030c83052deb1965d814f3)
- [ppc_is_vbus_sink](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gaf5e3999f3a016e33adf4797b62009d6d)
- [ppc_set_snk_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gae157ab53326686361309f20dfe5c4e64)
- [ppc_set_src_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gad38e1b5b5598c23ded44b343af58b791)
- [ppc_set_vbus_discharge](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gae66cb0377ffefabf85bc002a2fd04a47)
- [ppc_is_vbus_present](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gacd1ac1ac4ea60f16c58f57c9df11d536)
- [ppc_set_event_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#ga1d59cc94e8d303f0125fc88e5b447a69)
- [ppc_dump_regs](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__power__path__controller.html#gaeee650c29ce524b1e4d8ef66f295c1d7)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [usbc_ppc_driver_api::set_vbus_discharge](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#a1c2c21070ee18b7b5df09a6b6ed618b6)
- [usbc_ppc_driver_api::set_src_ctrl](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#a20ddefaee68808414f4075cc513a8660)
- [usbc_ppc_driver_api::exit_dead_battery_mode](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#a4ba2f654765130d5562f56243967bf58)
- [usbc_ppc_driver_api::is_dead_battery_mode](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#a832320573b2adab1d748e5e761690733)
- [usbc_ppc_driver_api::is_vbus_present](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#a8bf73dee9ba920f1b426038f62d5c9db)
- [usbc_ppc_driver_api::set_event_handler](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#a8f82ae3af5452d9cd0852bf15fcab573)
- [usbc_ppc_driver_api::is_vbus_sink](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#a93b91d21d4d2edda1d457f4144800f37)
- [usbc_ppc_driver_api::is_vbus_source](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#aab74a38a9c055efdfd0198143f12c9ff)
- [usbc_ppc_driver_api::dump_regs](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#adce51ae345d5fc417f3767476af36276)
- [usbc_ppc_driver_api::set_snk_ctrl](../device_power_control_model_reference/P100_usbc_ppc_driver_api_结构体.md#af4a66a11b66d48818123434c59553f0d)

---

[上一章](P237_usb_hid.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P239_usbd_hid.h_源码浏览.md)
