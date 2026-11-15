---
id: learning.zephyr-docs.api-source-pcie-hid-reference.page-8
title: sip_svc_controller.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__controller_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_sip\_svc\_controller.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__controller_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_supplement_reference/P113_zephyr__sip_svc__sip_svc_controller.h_文件参考.md)。

## 8.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="aatomic_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__thread__stack__api_html_ga600162959def399e70310b944834711f"></a>
<a id="akernel_2thread_8h_html_a6379f5a1f19ffbc262a6877c4f6e3647"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>

```c
/*
 * Copyright (c) 2023, Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_SIP_SVC_SIP_SVC_CONTROLLER_H_
#define ZEPHYR_INCLUDE_SIP_SVC_SIP_SVC_CONTROLLER_H_


#ifdef CONFIG_ARM_SIP_SVC_SUBSYS

#include <zephyr/sys/atomic.h>

#define SIP_SVC_SUBSYS_CONDUIT_NAME_LENGTH (4U)

enum open_state {
        SIP_SVC_OPEN_UNLOCKED = 0,
        SIP_SVC_OPEN_LOCKED
};

struct sip_svc_client {

        /* Client id internal to sip_svc*/
        uint32_t id;
        /* Client's token id provided back to client during sip_svc_register() */
        uint32_t token;
        /* Client's state */
        uint32_t state;
        /* Total Number of on-going transaction  of the client */
        uint32_t active_trans_cnt;
        /* Private data of each client , Provided during sip_svc_register() */
        void *priv_data;
        /* Transaction id pool for each client */
        struct sip_svc_id_pool *trans_idx_pool;
};

struct sip_svc_controller {

        /* Initialization status*/
        bool init;
        /* Total number of clients*/
        const uint32_t num_clients;
        /* Maximum allowable transactions in the system per controller*/
        const uint32_t max_transactions;
        /* Response size of buffer used for ASYNC transaction*/
        const uint32_t resp_size;
        /* Total Number of active transactions */
        uint32_t active_job_cnt;
        /* Active ASYNC transactions */
        uint32_t active_async_job_cnt;
        /* Supervisory call name , got from dts entry */
        char method[SIP_SVC_SUBSYS_CONDUIT_NAME_LENGTH];
        /* Pointer to driver instance */
        const struct device *dev;
        /* Pointer to client id pool */
        struct sip_svc_id_pool *client_id_pool;
        /* Pointer to database for storing arguments from sip_svc_send() */
        struct sip_svc_id_map *trans_id_map;
        /* Pointer to client array */
        struct sip_svc_client *clients;
        /* Pointer to Buffer used for storing response from lower layers */
        uint8_t *async_resp_data;
        /* Thread id of sip_svc thread */
        k_tid_t tid;

#if CONFIG_ARM_SIP_SVC_SUBSYS_SINGLY_OPEN
        /* Atomic variable to restrict one client access */
        atomic_t open_lock;
#endif
        /* Mutex for protecting database access */
        struct k_mutex data_mutex;
        /* msgq for sending sip_svc_request to sip_svc thread */
        struct k_msgq req_msgq;
        /* sip_svc thread object */
        struct k_thread thread;
        /* Stack object of sip_svc thread */
        K_KERNEL_STACK_MEMBER(stack, CONFIG_ARM_SIP_SVC_SUBSYS_THREAD_STACK_SIZE);
};

#define SIP_SVC_CONTROLLER_DEFINE(inst, conduit_name, sip_dev, sip_num_clients,                    \
                                  sip_max_transactions, sip_resp_size)                             \
        BUILD_ASSERT(                                                                              \
                ((sip_num_clients <= CONFIG_ARM_SIP_SVC_SUBSYS_MAX_CLIENT_COUNT) &&                \
                 (sip_num_clients > 0)),                                                           \
                "Number of client should be within 1 and ARM_SIP_SVC_SUBSYS_MAX_CLIENT_COUNT");    \
        static STRUCT_SECTION_ITERABLE(sip_svc_controller, sip_svc_##inst) = {                     \
                .method = conduit_name,                                                            \
                .dev = sip_dev,                                                                    \
                .num_clients = sip_num_clients,                                                    \
                .max_transactions = sip_max_transactions,                                          \
                .resp_size = sip_resp_size,                                                        \
        }

#else
#define SIP_SVC_CONTROLLER_DEFINE(inst, conduit_name, sip_dev, sip_num_clients,                    \
                                  sip_max_transactions, sip_resp_size)
#endif

#endif /* ZEPHYR_INCLUDE_SIP_SVC_SIP_SVC_CONTROLLER_H_ */
```

## 8.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023, Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 38 行

`sip_svc` 内部使用的客户端标识（Client ID）。

### 注释 3：原第 40 行

在 `sip_svc_register()` 期间返回给客户端的令牌标识（Token ID）。

### 注释 4：原第 42 行

客户端状态（Client State）。

### 注释 5：原第 44 行

客户端正在进行的事务（Transactions）总数。

### 注释 6：原第 46 行

各客户端的私有数据（Private Data），在 `sip_svc_register()` 期间提供。

### 注释 7：原第 48 行

每个客户端的事务标识池（Transaction ID Pool）。

### 注释 8：原第 58 行

初始化状态（Initialization Status）。

### 注释 9：原第 60 行

客户端总数（Total Number of Clients）。

### 注释 10：原第 62 行

系统中每个控制器允许的最大事务数（Maximum Transactions）。

### 注释 11：原第 64 行

用于异步事务（ASYNC Transaction）的缓冲区响应大小。

### 注释 12：原第 66 行

活动事务（Active Transactions）总数。

### 注释 13：原第 68 行

活动异步事务（Active ASYNC Transactions）。

### 注释 14：原第 70 行

从 DTS 条目取得的监控调用名称（Supervisory Call Name）。

### 注释 15：原第 72 行

指向驱动实例（Driver Instance）的指针。

### 注释 16：原第 74 行

指向客户端标识池（Client ID Pool）的指针。

### 注释 17：原第 76 行

指向数据库的指针，该数据库保存 `sip_svc_send()` 的参数。

### 注释 18：原第 78 行

指向客户端数组（Client Array）的指针。

### 注释 19：原第 80 行

指向缓冲区的指针，该缓冲区保存下层返回的响应（Response）。

### 注释 20：原第 82 行

`sip_svc` 线程的线程标识（Thread ID）。

### 注释 21：原第 86 行

用于将访问限制为单个客户端的原子变量（Atomic Variable）。

### 注释 22：原第 89 行

保护数据库访问的互斥锁（Mutex）。

### 注释 23：原第 91 行

向 `sip_svc` 线程发送 `sip_svc_request` 的消息队列（Message Queue）。

### 注释 24：原第 93 行

`sip_svc` 线程对象（Thread Object）。

### 注释 25：原第 95 行

`sip_svc` 线程的栈对象（Stack Object）。

### 注释 26：原第 123 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SIP_SVC_SIP_SVC_CONTROLLER_H_`。

## 8.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_supplement_reference/P113_zephyr__sip_svc__sip_svc_controller.h_文件参考.md)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [K_KERNEL_STACK_MEMBER](../thread_stack_reference/P001_线程栈接口.md#ga600162959def399e70310b944834711f)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)

---

[上一章](P007_mfd_ite_it8801.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P009_hid.h_源码浏览.md)
