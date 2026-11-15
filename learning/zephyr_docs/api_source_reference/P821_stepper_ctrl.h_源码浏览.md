---
id: learning.zephyr-docs.api-source-reference.page-821
title: stepper_ctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stepper__ctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第821章\_stepper\_ctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stepper__ctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stepper__ctrl_8h.html)。

## 821.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00045"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="foldopen00057"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="foldopen00071"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00090"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="foldopen00168"></a>
<a id="l00168"></a>
<a id="l00172"></a>
<a id="l00176"></a>
<a id="l00180"></a>
<a id="l00184"></a>
<a id="l00188"></a>
<a id="l00192"></a>
<a id="l00196"></a>
<a id="l00200"></a>
<a id="l00204"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00214"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
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
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__stepper__ctrl__backend_html_ga0d807a6415c0040fcf493d5c9c3fa5b1"></a>
<a id="agroup__stepper__ctrl__backend_html_ga142d6eecbaead22de75e3e3d69e23550"></a>
<a id="agroup__stepper__ctrl__backend_html_ga1570a86e75fbcecfc63213cd144b4a5b"></a>
<a id="agroup__stepper__ctrl__backend_html_ga2dbdb4e8b581e3766866f7e9435c3429"></a>
<a id="agroup__stepper__ctrl__backend_html_ga719f13485d6c74a365e69661b3f02abe"></a>
<a id="agroup__stepper__ctrl__backend_html_ga8bba3a3304eece57b9047e5f5d2e2fc4"></a>
<a id="agroup__stepper__ctrl__backend_html_gab3a7b8c29e066fc8e4a0333fb7098992"></a>
<a id="agroup__stepper__ctrl__backend_html_gac78bf81389bd3013fea18caca0e77e54"></a>
<a id="agroup__stepper__ctrl__backend_html_gadc066df6951f3bffed3de0d922588842"></a>
<a id="agroup__stepper__ctrl__backend_html_gaef2903403ded0b2b60e56bd8412a4938"></a>
<a id="agroup__stepper__ctrl_html_ga188b64bc308fb78a77cfdcf4bfe1b5f7"></a>
<a id="agroup__stepper__ctrl_html_ga1cb888e11712c54bd879a5b0015ea298"></a>
<a id="agroup__stepper__ctrl_html_ga544a15b5df405c08127fa8529cfbcf0b"></a>
<a id="agroup__stepper__ctrl_html_ga61dfffaeb3d7f76c34c9a9e3ab7627d0"></a>
<a id="agroup__stepper__ctrl_html_ga69198946de2a596894b1fc26a13a4c58"></a>
<a id="agroup__stepper__ctrl_html_ga780784ec0b192e68849627ff97116c78"></a>
<a id="agroup__stepper__ctrl_html_ga81a1a98c7381cf5845d9e6a908bdd4a5"></a>
<a id="agroup__stepper__ctrl_html_gaa968ec0a373206d239ac96abc20ee9ea"></a>
<a id="agroup__stepper__ctrl_html_gac264384ffdd5c4eca154ddf941abf8a5"></a>
<a id="agroup__stepper__ctrl_html_gacd154f195a34a0de50ab26c81ce469d8"></a>
<a id="agroup__stepper__ctrl_html_gae0ebe9949b9fe2bda51c4dc9d537cac5"></a>
<a id="agroup__stepper__ctrl_html_gae723aee1b73b3b65d8ead0546b976cd0"></a>
<a id="agroup__stepper__ctrl_html_gae78e47cb34035887cf4e8c6a7c6de9de"></a>
<a id="agroup__stepper__ctrl_html_gaf2c33e8fcf6cd03dfb9361c0246281fb"></a>
<a id="agroup__stepper__ctrl_html_gga188b64bc308fb78a77cfdcf4bfe1b5f7a339a2080488f0395a791586b0e6b0330"></a>
<a id="agroup__stepper__ctrl_html_gga188b64bc308fb78a77cfdcf4bfe1b5f7a3a7272f5a1643140271b009d848d63d8"></a>
<a id="agroup__stepper__ctrl_html_gga61dfffaeb3d7f76c34c9a9e3ab7627d0a3339b85fb6aafe8d96b47a1fcc2be21c"></a>
<a id="agroup__stepper__ctrl_html_gga61dfffaeb3d7f76c34c9a9e3ab7627d0a391d21e562f172dfd5e554b7540e24a0"></a>
<a id="agroup__stepper__ctrl_html_gga61dfffaeb3d7f76c34c9a9e3ab7627d0abcdf3ebb12e2452b8dd97a78f7799fa3"></a>
<a id="agroup__stepper__ctrl_html_gga61dfffaeb3d7f76c34c9a9e3ab7627d0ae8d633746759b9399dc149a1b31429a3"></a>
<a id="agroup__stepper__ctrl_html_gga81a1a98c7381cf5845d9e6a908bdd4a5a5dadeff6f35458f9310744e9b6e305b7"></a>
<a id="agroup__stepper__ctrl_html_gga81a1a98c7381cf5845d9e6a908bdd4a5aa7bd6559d26845de9cba1e1a15a1d841"></a>
<a id="agroup__stepper__ctrl_html_gga81a1a98c7381cf5845d9e6a908bdd4a5ab5ab3be4513a981e070c65dffac633ad"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astructdevice_html"></a>
<a id="astructstepper__ctrl__driver__api_html"></a>
<a id="astructstepper__ctrl__driver__api_html_a058eefb88ce723f7f564b3962cd98849"></a>
<a id="astructstepper__ctrl__driver__api_html_a1637f22d5558a1dce320397cfff04963"></a>
<a id="astructstepper__ctrl__driver__api_html_a25203d56f47174b109d0e9314db60914"></a>
<a id="astructstepper__ctrl__driver__api_html_a45281e899fc4fe6f9682a6868260154a"></a>
<a id="astructstepper__ctrl__driver__api_html_a469a8631d79f3ba7790a541ce0b2e468"></a>
<a id="astructstepper__ctrl__driver__api_html_a663ed6664264de124fcd55cadfecc657"></a>
<a id="astructstepper__ctrl__driver__api_html_a9fb7bac73c7d8e1e93128dcd5e989d54"></a>
<a id="astructstepper__ctrl__driver__api_html_ae42f0b1739c344b3a21108cdb378621c"></a>
<a id="astructstepper__ctrl__driver__api_html_af71d30bad10d0fd3f6ecd9fa26231bae"></a>
<a id="astructstepper__ctrl__driver__api_html_afff45f706a25d44719b5c322b8e156b2"></a>
<a id="astructstepper__ctrl__ramp_html"></a>
<a id="astructstepper__ctrl__ramp_html_a3975a535adcf407c19ae9ab804b73efe"></a>
<a id="astructstepper__ctrl__ramp_html_ad14c31f2db1191e46585b03edcc14719"></a>
<a id="astructstepper__ctrl__ramp_html_ae3348ab71b3f686c0cb872c7d65dee29"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2025 Jilay Sandeep Pandya
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_STEPPER_CTRL_H_
#define ZEPHYR_INCLUDE_DRIVERS_STEPPER_CTRL_H_


#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <errno.h>

#ifdef __cplusplus
extern "C" {
#endif

enum stepper_ctrl_direction {
        STEPPER_CTRL_DIRECTION_NEGATIVE = 0,
        STEPPER_CTRL_DIRECTION_POSITIVE = 1,
};

enum stepper_ctrl_run_mode {
        STEPPER_CTRL_RUN_MODE_HOLD = 0,
        STEPPER_CTRL_RUN_MODE_POSITION = 1,
        STEPPER_CTRL_RUN_MODE_VELOCITY = 2,
};

enum stepper_ctrl_event {
        STEPPER_CTRL_EVENT_STEPS_COMPLETED = 0,
        STEPPER_CTRL_EVENT_LEFT_END_STOP_DETECTED = 1,
        STEPPER_CTRL_EVENT_RIGHT_END_STOP_DETECTED = 2,
        STEPPER_CTRL_EVENT_STOPPED = 3,
};

struct stepper_ctrl_ramp {
        uint32_t acceleration_max;
        uint32_t speed_max;
        uint32_t deceleration_max;
};

typedef void (*stepper_ctrl_event_callback_t)(const struct device *dev,
                                              const enum stepper_ctrl_event event, void *user_data);


typedef int (*stepper_ctrl_set_reference_position_t)(const struct device *dev, const int32_t value);

typedef int (*stepper_ctrl_get_actual_position_t)(const struct device *dev, int32_t *value);

typedef int (*stepper_ctrl_set_event_cb_t)(const struct device *dev,
                                           stepper_ctrl_event_callback_t callback, void *user_data);

typedef int (*stepper_ctrl_set_microstep_interval_t)(const struct device *dev,
                                                     const uint64_t microstep_interval_ns);

typedef int (*stepper_ctrl_configure_ramp_t)(const struct device *dev,
                                             const struct stepper_ctrl_ramp *ramp);

typedef int (*stepper_ctrl_move_by_t)(const struct device *dev, const int32_t micro_steps);

typedef int (*stepper_ctrl_move_to_t)(const struct device *dev, const int32_t micro_steps);

typedef int (*stepper_ctrl_run_t)(const struct device *dev,
                                  const enum stepper_ctrl_direction direction);

typedef int (*stepper_ctrl_stop_t)(const struct device *dev);

typedef int (*stepper_ctrl_is_moving_t)(const struct device *dev, bool *is_moving);

__subsystem struct stepper_ctrl_driver_api {
        stepper_ctrl_set_reference_position_t set_reference_position;
        stepper_ctrl_get_actual_position_t get_actual_position;
        stepper_ctrl_set_event_cb_t set_event_cb;
        stepper_ctrl_set_microstep_interval_t set_microstep_interval;
        stepper_ctrl_configure_ramp_t configure_ramp;
        stepper_ctrl_move_by_t move_by;
        stepper_ctrl_move_to_t move_to;
        stepper_ctrl_run_t run;
        stepper_ctrl_stop_t stop;
        stepper_ctrl_is_moving_t is_moving;
};


__syscall int stepper_ctrl_set_reference_position(const struct device *dev, const int32_t value);

static inline int z_impl_stepper_ctrl_set_reference_position(const struct device *dev,
                                                             const int32_t value)
{
        if (DEVICE_API_GET(stepper_ctrl, dev)->set_reference_position == NULL) {
                return -ENOSYS;
        }
        return DEVICE_API_GET(stepper_ctrl, dev)->set_reference_position(dev, value);
}


__syscall int stepper_ctrl_get_actual_position(const struct device *dev, int32_t *value);

static inline int z_impl_stepper_ctrl_get_actual_position(const struct device *dev, int32_t *value)
{
        __ASSERT_NO_MSG(value != NULL);

        if (DEVICE_API_GET(stepper_ctrl, dev)->get_actual_position == NULL) {
                return -ENOSYS;
        }
        return DEVICE_API_GET(stepper_ctrl, dev)->get_actual_position(dev, value);
}


__syscall int stepper_ctrl_set_event_cb(const struct device *dev,
                                        stepper_ctrl_event_callback_t callback, void *user_data);

static inline int z_impl_stepper_ctrl_set_event_cb(const struct device *dev,
                                                   stepper_ctrl_event_callback_t callback,
                                                   void *user_data)
{
        if (DEVICE_API_GET(stepper_ctrl, dev)->set_event_cb == NULL) {
                return -ENOSYS;
        }
        return DEVICE_API_GET(stepper_ctrl, dev)->set_event_cb(dev, callback, user_data);
}

__syscall int stepper_ctrl_set_microstep_interval(const struct device *dev,
                                                  const uint64_t microstep_interval_ns);

static inline int z_impl_stepper_ctrl_set_microstep_interval(const struct device *dev,
                                                             const uint64_t microstep_interval_ns)
{
        if (DEVICE_API_GET(stepper_ctrl, dev)->set_microstep_interval == NULL) {
                return -ENOSYS;
        }
        return DEVICE_API_GET(stepper_ctrl, dev)->set_microstep_interval(dev,
                                                                      microstep_interval_ns);
}

__syscall int stepper_ctrl_configure_ramp(const struct device *dev,
                                          const struct stepper_ctrl_ramp *ramp);

static inline int z_impl_stepper_ctrl_configure_ramp(const struct device *dev,
        const struct stepper_ctrl_ramp *ramp)
{
        __ASSERT_NO_MSG(ramp != NULL);

        if (DEVICE_API_GET(stepper_ctrl, dev)->configure_ramp == NULL) {
                return -ENOSYS;
        }
        return DEVICE_API_GET(stepper_ctrl, dev)->configure_ramp(dev, ramp);
}
__syscall int stepper_ctrl_move_by(const struct device *dev, const int32_t micro_steps);

static inline int z_impl_stepper_ctrl_move_by(const struct device *dev, const int32_t micro_steps)
{
        return DEVICE_API_GET(stepper_ctrl, dev)->move_by(dev, micro_steps);
}

__syscall int stepper_ctrl_move_to(const struct device *dev, const int32_t micro_steps);

static inline int z_impl_stepper_ctrl_move_to(const struct device *dev, const int32_t micro_steps)
{
        return DEVICE_API_GET(stepper_ctrl, dev)->move_to(dev, micro_steps);
}

__syscall int stepper_ctrl_run(const struct device *dev,
                               const enum stepper_ctrl_direction direction);

static inline int z_impl_stepper_ctrl_run(const struct device *dev,
                                          const enum stepper_ctrl_direction direction)
{
        if (DEVICE_API_GET(stepper_ctrl, dev)->run == NULL) {
                return -ENOSYS;
        }
        return DEVICE_API_GET(stepper_ctrl, dev)->run(dev, direction);
}

__syscall int stepper_ctrl_stop(const struct device *dev);

static inline int z_impl_stepper_ctrl_stop(const struct device *dev)
{
        if (DEVICE_API_GET(stepper_ctrl, dev)->stop == NULL) {
                return -ENOSYS;
        }
        return DEVICE_API_GET(stepper_ctrl, dev)->stop(dev);
}

__syscall int stepper_ctrl_is_moving(const struct device *dev, bool *is_moving);

static inline int z_impl_stepper_ctrl_is_moving(const struct device *dev, bool *is_moving)
{
        __ASSERT_NO_MSG(is_moving != NULL);
        if (DEVICE_API_GET(stepper_ctrl, dev)->is_moving == NULL) {
                return -ENOSYS;
        }
        return DEVICE_API_GET(stepper_ctrl, dev)->is_moving(dev, is_moving);
}


#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/stepper_ctrl.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_STEPPER_CTRL_H_ */
```

## 821.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2025 Jilay Sandeep Pandya。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 455 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_STEPPER_CTRL_H_`。

## 821.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stepper__ctrl_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [stepper_ctrl_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga188b64bc308fb78a77cfdcf4bfe1b5f7)
- [STEPPER_CTRL_DIRECTION_NEGATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga188b64bc308fb78a77cfdcf4bfe1b5f7a3a7272f5a1643140271b009d848d63d8)
- [STEPPER_CTRL_DIRECTION_POSITIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga188b64bc308fb78a77cfdcf4bfe1b5f7a339a2080488f0395a791586b0e6b0330)
- [stepper_ctrl_run_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga81a1a98c7381cf5845d9e6a908bdd4a5)
- [STEPPER_CTRL_RUN_MODE_HOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga81a1a98c7381cf5845d9e6a908bdd4a5a5dadeff6f35458f9310744e9b6e305b7)
- [STEPPER_CTRL_RUN_MODE_POSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga81a1a98c7381cf5845d9e6a908bdd4a5aa7bd6559d26845de9cba1e1a15a1d841)
- [STEPPER_CTRL_RUN_MODE_VELOCITY](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga81a1a98c7381cf5845d9e6a908bdd4a5ab5ab3be4513a981e070c65dffac633ad)
- [stepper_ctrl_event](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga61dfffaeb3d7f76c34c9a9e3ab7627d0)
- [STEPPER_CTRL_EVENT_STEPS_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga61dfffaeb3d7f76c34c9a9e3ab7627d0abcdf3ebb12e2452b8dd97a78f7799fa3)
- [STEPPER_CTRL_EVENT_LEFT_END_STOP_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga61dfffaeb3d7f76c34c9a9e3ab7627d0a391d21e562f172dfd5e554b7540e24a0)
- [STEPPER_CTRL_EVENT_RIGHT_END_STOP_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga61dfffaeb3d7f76c34c9a9e3ab7627d0a3339b85fb6aafe8d96b47a1fcc2be21c)
- [STEPPER_CTRL_EVENT_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gga61dfffaeb3d7f76c34c9a9e3ab7627d0ae8d633746759b9399dc149a1b31429a3)
- [stepper_ctrl_ramp](../hardware/P231_步进速度斜坡结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [acceleration_max](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__ramp.html#ad14c31f2db1191e46585b03edcc14719)
- [speed_max](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__ramp.html#ae3348ab71b3f686c0cb872c7d65dee29)
- [deceleration_max](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__ramp.html#a3975a535adcf407c19ae9ab804b73efe)
- [stepper_ctrl_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga69198946de2a596894b1fc26a13a4c58)
- [device](../device_reference/P002_设备对象结构.md)
- [stepper_ctrl_set_reference_position_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga142d6eecbaead22de75e3e3d69e23550)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [stepper_ctrl_get_actual_position_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga0d807a6415c0040fcf493d5c9c3fa5b1)
- [stepper_ctrl_set_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga1570a86e75fbcecfc63213cd144b4a5b)
- [stepper_ctrl_set_microstep_interval_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#gac78bf81389bd3013fea18caca0e77e54)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [stepper_ctrl_configure_ramp_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga719f13485d6c74a365e69661b3f02abe)
- [stepper_ctrl_move_by_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#gab3a7b8c29e066fc8e4a0333fb7098992)
- [stepper_ctrl_move_to_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga8bba3a3304eece57b9047e5f5d2e2fc4)
- [stepper_ctrl_run_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#ga2dbdb4e8b581e3766866f7e9435c3429)
- [stepper_ctrl_stop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#gaef2903403ded0b2b60e56bd8412a4938)
- [stepper_ctrl_is_moving_t](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl__backend.html#gadc066df6951f3bffed3de0d922588842)
- [stepper_ctrl_driver_api](../hardware/P234_步进运动控制函数表.md)
- [set_reference_position](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#a25203d56f47174b109d0e9314db60914)
- [get_actual_position](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#afff45f706a25d44719b5c322b8e156b2)
- [set_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#a469a8631d79f3ba7790a541ce0b2e468)
- [set_microstep_interval](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#a663ed6664264de124fcd55cadfecc657)
- [configure_ramp](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#af71d30bad10d0fd3f6ecd9fa26231bae)
- [move_by](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#a1637f22d5558a1dce320397cfff04963)
- [move_to](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#ae42f0b1739c344b3a21108cdb378621c)
- [run](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#a9fb7bac73c7d8e1e93128dcd5e989d54)
- [stop](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#a058eefb88ce723f7f564b3962cd98849)
- [is_moving](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#a45281e899fc4fe6f9682a6868260154a)
- [stepper_ctrl_set_reference_position](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gae723aee1b73b3b65d8ead0546b976cd0)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [stepper_ctrl_get_actual_position](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gaf2c33e8fcf6cd03dfb9361c0246281fb)
- [stepper_ctrl_set_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gacd154f195a34a0de50ab26c81ce469d8)
- [stepper_ctrl_set_microstep_interval](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga1cb888e11712c54bd879a5b0015ea298)
- [stepper_ctrl_configure_ramp](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gae0ebe9949b9fe2bda51c4dc9d537cac5)
- [stepper_ctrl_move_by](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gaa968ec0a373206d239ac96abc20ee9ea)
- [stepper_ctrl_move_to](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gac264384ffdd5c4eca154ddf941abf8a5)
- [stepper_ctrl_run](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga544a15b5df405c08127fa8529cfbcf0b)
- [stepper_ctrl_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga780784ec0b192e68849627ff97116c78)
- [stepper_ctrl_is_moving](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gae78e47cb34035887cf4e8c6a7c6de9de)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [stepper_ctrl_driver_api::stop](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#a058eefb88ce723f7f564b3962cd98849)
- [stepper_ctrl_driver_api::move_by](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#a1637f22d5558a1dce320397cfff04963)
- [stepper_ctrl_driver_api::set_reference_position](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#a25203d56f47174b109d0e9314db60914)
- [stepper_ctrl_driver_api::is_moving](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#a45281e899fc4fe6f9682a6868260154a)
- [stepper_ctrl_driver_api::set_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#a469a8631d79f3ba7790a541ce0b2e468)
- [stepper_ctrl_driver_api::set_microstep_interval](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#a663ed6664264de124fcd55cadfecc657)
- [stepper_ctrl_driver_api::run](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#a9fb7bac73c7d8e1e93128dcd5e989d54)
- [stepper_ctrl_driver_api::move_to](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#ae42f0b1739c344b3a21108cdb378621c)
- [stepper_ctrl_driver_api::configure_ramp](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#af71d30bad10d0fd3f6ecd9fa26231bae)
- [stepper_ctrl_driver_api::get_actual_position](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__driver__api.html#afff45f706a25d44719b5c322b8e156b2)
- [stepper_ctrl_ramp::deceleration_max](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__ramp.html#a3975a535adcf407c19ae9ab804b73efe)
- [stepper_ctrl_ramp::acceleration_max](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__ramp.html#ad14c31f2db1191e46585b03edcc14719)
- [stepper_ctrl_ramp::speed_max](https://docs.zephyrproject.org/latest/doxygen/html/structstepper__ctrl__ramp.html#ae3348ab71b3f686c0cb872c7d65dee29)

---

[上一章](P820_stepper.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P822_stepper_drv84xx.h_源码浏览.md)
