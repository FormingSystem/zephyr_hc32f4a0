---
id: learning.zephyr-docs.intercore_reference.zbuscoreref-212
title: zbus核心完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/zbus_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第212章\_zbus核心完整头文件

原文：[zbus_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/zbus_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留`zephyr/zbus/zbus.h`的完整官方可见源码（Source Code），仅去除网页行号与行尾空白。2022年 Rodrigo Peixoto 的版权、邮箱及`Apache-2.0`许可证（License）原声明完整保留。

API 指应用程序编程接口（Application Programming Interface）。zbus 为消息总线（Message Bus），Channel 为通道，Observer 为观察者，Listener 为监听器，Subscriber 为订阅者，Callback 为回调，Validator 为验证器，Work Queue 为工作队列，Semaphore 为信号量，FIFO 为先进先出队列（First In, First Out）。`CONFIG_`配置宏来自 Kconfig 构建配置系统（Build Configuration System）。

结构、条件字段和接口索引分别见[zbus通道结构](P206_zbus通道结构.md)、[zbus通道运行时结构](P207_zbus通道运行时结构.md)、[zbus观察者结构](P208_zbus观察者结构.md)、[zbus运行时观察者节点](P209_zbus运行时观察者节点.md)、[zbus运行时通道结构](P210_zbus运行时通道结构.md)、[zbus核心头文件参考](P211_zbus核心头文件参考.md)，全部调用约束、参数与错误码见[zbus核心接口](P213_zbus核心接口.md)。

## 212.1\_完整源码

下面保持整份头文件为一个连续代码块，保留条件分支和宏续行，便于与官方源码对照。

```c
/*
 * Copyright (c) 2022 Rodrigo Peixoto <rodrigopex@gmail.com>
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_ZBUS_ZBUS_H_
#define ZEPHYR_INCLUDE_ZBUS_ZBUS_H_

#include <string.h>

#include <zephyr/kernel.h>
#include <zephyr/sys/check.h>
#include <zephyr/sys/iterable_sections.h>

#ifdef __cplusplus
extern "C" {
#endif


struct zbus_channel_data {

        int16_t observers_start_idx;

        int16_t observers_end_idx;

        struct k_sem sem;

#if defined(CONFIG_ZBUS_PRIORITY_BOOST)
        int highest_observer_priority;
#endif /* CONFIG_ZBUS_PRIORITY_BOOST */

#if defined(CONFIG_ZBUS_RUNTIME_OBSERVERS) || defined(__DOXYGEN__)
        sys_slist_t observers;
#endif /* CONFIG_ZBUS_RUNTIME_OBSERVERS */

#if defined(CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION) || defined(__DOXYGEN__)
        struct net_buf_pool *msg_subscriber_pool;
#endif /* ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION */

#if defined(CONFIG_ZBUS_CHANNEL_PUBLISH_STATS) || defined(__DOXYGEN__)
        k_ticks_t publish_timestamp;
        uint32_t publish_count;
#endif /* CONFIG_ZBUS_CHANNEL_PUBLISH_STATS */

};

typedef bool (*zbus_validator)(const void *msg, size_t msg_size);

struct zbus_channel {
#if defined(CONFIG_ZBUS_CHANNEL_NAME) || defined(__DOXYGEN__)
        const char *name;
#endif
#if defined(CONFIG_ZBUS_CHANNEL_ID) || defined(__DOXYGEN__)
        uint32_t id;
#endif
        void *message;

        size_t message_size;

        void *user_data;

        zbus_validator validator;

        struct zbus_channel_data *data;
};

struct zbus_runtime_channel {
        struct zbus_channel channel;
        sys_snode_t _node;
};

enum __packed zbus_observer_type {
        ZBUS_OBSERVER_LISTENER_TYPE,
        ZBUS_OBSERVER_SUBSCRIBER_TYPE,
        ZBUS_OBSERVER_MSG_SUBSCRIBER_TYPE,
        ZBUS_OBSERVER_ASYNC_LISTENER_TYPE,
};

struct zbus_observer_data {
        bool enabled;

#if defined(CONFIG_ZBUS_PRIORITY_BOOST)
        int priority;
#endif /* CONFIG_ZBUS_PRIORITY_BOOST */
};

struct zbus_observer {
#if defined(CONFIG_ZBUS_OBSERVER_NAME) || defined(__DOXYGEN__)
        const char *name;
#endif
        enum zbus_observer_type type;

        struct zbus_observer_data *data;

        union {
                struct k_msgq *queue;

                void (*callback)(const struct zbus_channel *chan);

#if defined(CONFIG_ZBUS_MSG_SUBSCRIBER) || defined(__DOXYGEN__)
                struct k_fifo *message_fifo;
#endif /* CONFIG_ZBUS_MSG_SUBSCRIBER */

#if defined(CONFIG_ZBUS_ASYNC_LISTENER) || defined(__DOXYGEN__)
                struct k_work *work;
#endif /* CONFIG_ZBUS_ASYNC_LISTENER */
        };
};

struct zbus_channel_observation_mask {
        bool enabled;
};

struct zbus_channel_observation {
        const struct zbus_channel *chan;
        const struct zbus_observer *obs;
};

#ifdef __cplusplus
#define _ZBUS_CPP_EXTERN extern
#else
#define _ZBUS_CPP_EXTERN
#endif /* __cplusplus */

#define ZBUS_MIN_THREAD_PRIORITY (CONFIG_NUM_PREEMPT_PRIORITIES - 1)

#if defined(CONFIG_ZBUS_ASSERT_MOCK)
#define _ZBUS_ASSERT(_cond, _fmt, ...)                                                             \
        do {                                                                                       \
                if (!(_cond)) {                                                                    \
                        printk("ZBUS ASSERT: ");                                                   \
                        printk(_fmt, ##__VA_ARGS__);                                               \
                        printk("\n");                                                              \
                        return -EFAULT;                                                            \
                }                                                                                  \
        } while (0)
#else
#define _ZBUS_ASSERT(_cond, _fmt, ...) __ASSERT(_cond, _fmt, ##__VA_ARGS__)
#endif

#if defined(CONFIG_ZBUS_CHANNEL_NAME)
#define ZBUS_CHANNEL_NAME_INIT(_name) .name = #_name,
#define _ZBUS_CHAN_NAME(_chan)        (_chan)->name
#else
#define ZBUS_CHANNEL_NAME_INIT(_name)
#define _ZBUS_CHAN_NAME(_chan) ""
#endif

#if defined(CONFIG_ZBUS_OBSERVER_NAME)
#define ZBUS_OBSERVER_NAME_INIT(_name) .name = #_name,
#define _ZBUS_OBS_NAME(_obs)           (_obs)->name
#else
#define ZBUS_OBSERVER_NAME_INIT(_name)
#define _ZBUS_OBS_NAME(_obs) ""
#endif

#if defined(CONFIG_ZBUS_RUNTIME_OBSERVERS)
#define ZBUS_RUNTIME_OBSERVERS_LIST_DECL(_slist_name) static sys_slist_t _slist_name
#define ZBUS_RUNTIME_OBSERVERS_LIST_INIT(_slist_name) .runtime_observers = &_slist_name,
#else
#define ZBUS_RUNTIME_OBSERVERS_LIST_DECL(_slist_name)
#define ZBUS_RUNTIME_OBSERVERS_LIST_INIT(_slist_name) /* No runtime observers */
#endif

#define _ZBUS_OBS_EXTERN(_name) extern const struct zbus_observer _name

#define _ZBUS_CHAN_EXTERN(_name) extern const struct zbus_channel _name

#define ZBUS_REF(_value) &(_value)

#define FOR_EACH_FIXED_ARG_NONEMPTY_TERM(F, sep, fixed_arg, ...)                                   \
        COND_CODE_0(/* are there zero non-empty arguments ? */                                     \
                    NUM_VA_ARGS_LESS_1(                                                            \
                            LIST_DROP_EMPTY(__VA_ARGS__, _)), /* if so, expand to nothing */       \
                    (),                                       /* otherwise, expand to: */          \
                    (FOR_EACH_IDX_FIXED_ARG(                                                       \
                            F, sep, fixed_arg,                                                     \
                            LIST_DROP_EMPTY(__VA_ARGS__)) /* plus a final terminator */            \
                     __DEBRACKET sep))

#define _ZBUS_OBSERVATION_PREFIX(_idx)                                                             \
        GET_ARG_N(_idx, 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17,    \
                  18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,  \
                  38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,  \
                  58, 59, 60, 61, 62, 63)

#define _ZBUS_CHAN_OBSERVATION(_idx, _obs, _chan)                                                  \
        const STRUCT_SECTION_ITERABLE(                                                             \
                zbus_channel_observation,                                                          \
                _CONCAT(_chan, _ZBUS_OBSERVATION_PREFIX(UTIL_INC(_idx)))) = {.chan = &_chan,       \
                                                                             .obs = &_obs};        \
        STRUCT_SECTION_ITERABLE(zbus_channel_observation_mask,                                     \
                                _CONCAT(_CONCAT(_chan, _ZBUS_OBSERVATION_PREFIX(UTIL_INC(_idx))),  \
                                        _mask)) = {.enabled = false};

#if defined(CONFIG_ZBUS_RUNTIME_OBSERVERS) || defined(__DOXYGEN__)
#define _ZBUS_RUNTIME_OBSERVERS(_name)      .observers = &(_CONCAT(_observers_, _name)),
#define _ZBUS_RUNTIME_OBSERVERS_DECL(_name) static sys_slist_t _CONCAT(_observers_, _name);
#else
#define _ZBUS_RUNTIME_OBSERVERS(_name)
#define _ZBUS_RUNTIME_OBSERVERS_DECL(_name)
#endif /* CONFIG_ZBUS_RUNTIME_OBSERVERS */

#define _ZBUS_MESSAGE_NAME(_name) _CONCAT(_zbus_message_, _name)

/* clang-format off */
#define _ZBUS_CHAN_DEFINE(_name, _id, _type, _validator, _user_data)                               \
        static struct zbus_channel_data _CONCAT(_zbus_chan_data_, _name) = {                       \
                .observers_start_idx = -1,                                                         \
                .observers_end_idx = -1,                                                           \
                .sem = Z_SEM_INITIALIZER(_CONCAT(_zbus_chan_data_, _name).sem, 1, 1),              \
                IF_ENABLED(CONFIG_ZBUS_PRIORITY_BOOST,                                             \
                           (.highest_observer_priority = ZBUS_MIN_THREAD_PRIORITY,))               \
                IF_ENABLED(CONFIG_ZBUS_RUNTIME_OBSERVERS,                                          \
                           (.observers = SYS_SLIST_STATIC_INIT(                                    \
                                &_CONCAT(_zbus_chan_data_, _name).observers),))                    \
                IF_ENABLED(CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION,                      \
                           (.msg_subscriber_pool = NULL,))                                         \
        };                                                                                         \
        _ZBUS_CPP_EXTERN const STRUCT_SECTION_ITERABLE(zbus_channel, _name) = {                    \
                ZBUS_CHANNEL_NAME_INIT(_name) /* Maybe removed */                                  \
                IF_ENABLED(CONFIG_ZBUS_CHANNEL_ID, (.id = _id,))                                   \
                .message = &_ZBUS_MESSAGE_NAME(_name),                                             \
                .message_size = sizeof(_type),                                                     \
                .user_data = _user_data,                                                           \
                .validator = _validator,                                                           \
                .data = &_CONCAT(_zbus_chan_data_, _name),                                         \
        }
/* clang-format on */


/* clang-format off */

#define ZBUS_CHAN_ADD_OBS_WITH_MASK(_chan, _obs, _masked, _prio)                                   \
        const STRUCT_SECTION_ITERABLE(zbus_channel_observation,                                    \
                _CONCAT(_CONCAT(_chan, zz), _CONCAT(_prio, _obs))) = {                             \
                        .chan = &_chan,                                                            \
                        .obs = &_obs,                                                              \
        };                                                                                         \
        STRUCT_SECTION_ITERABLE(zbus_channel_observation_mask,                                     \
                                _CONCAT(_CONCAT(_CONCAT(_chan, zz), _CONCAT(_prio, _obs)),         \
                                        _mask)) = {.enabled = _masked}
/* clang-format on */

#define ZBUS_CHAN_ADD_OBS(_chan, _obs, _prio) ZBUS_CHAN_ADD_OBS_WITH_MASK(_chan, _obs, false, _prio)

#define ZBUS_OBS_DECLARE(...) FOR_EACH_NONEMPTY_TERM(_ZBUS_OBS_EXTERN, (;), __VA_ARGS__)

#define ZBUS_CHAN_DECLARE(...) FOR_EACH(_ZBUS_CHAN_EXTERN, (;), __VA_ARGS__)

#define ZBUS_OBSERVERS_EMPTY

#define ZBUS_OBSERVERS(...) __VA_ARGS__

#define ZBUS_CHAN_ID_INVALID UINT32_MAX

#define ZBUS_CHAN_DEFINE(_name, _type, _validator, _user_data, _observers, _init_val)              \
        static _type _ZBUS_MESSAGE_NAME(_name) = _init_val;                                        \
        _ZBUS_CHAN_DEFINE(_name, ZBUS_CHAN_ID_INVALID, _type, _validator, _user_data);             \
        /* Extern declaration of observers */                                                      \
        ZBUS_OBS_DECLARE(_observers);                                                              \
        /* Create all channel observations from observers list */                                  \
        FOR_EACH_FIXED_ARG_NONEMPTY_TERM(_ZBUS_CHAN_OBSERVATION, (;), _name, _observers)

#define ZBUS_CHAN_DEFINE_WITH_ID(_name, _id, _type, _validator, _user_data, _observers, _init_val) \
        static _type _ZBUS_MESSAGE_NAME(_name) = _init_val;                                        \
        _ZBUS_CHAN_DEFINE(_name, _id, _type, _validator, _user_data);                              \
        /* Extern declaration of observers */                                                      \
        ZBUS_OBS_DECLARE(_observers);                                                              \
        /* Create all channel observations from observers list */                                  \
        FOR_EACH_FIXED_ARG_NONEMPTY_TERM(_ZBUS_CHAN_OBSERVATION, (;), _name, _observers)

#define ZBUS_MSG_INIT(_val, ...) {_val, ##__VA_ARGS__}

/* clang-format off */

#define ZBUS_SUBSCRIBER_DEFINE_WITH_ENABLE(_name, _queue_size, _enable)       \
        K_MSGQ_DEFINE_STATIC_TYPE(_zbus_observer_queue_##_name,               \
                                  struct zbus_channel *, _queue_size          \
        );                                                                    \
        static struct zbus_observer_data _CONCAT(_zbus_obs_data_, _name) = {  \
                .enabled = _enable,                                           \
                IF_ENABLED(CONFIG_ZBUS_PRIORITY_BOOST, (                      \
                        .priority = ZBUS_MIN_THREAD_PRIORITY,                 \
                ))                                                            \
        };                                                                    \
        _ZBUS_CPP_EXTERN const STRUCT_SECTION_ITERABLE(zbus_observer, _name) = {  \
                ZBUS_OBSERVER_NAME_INIT(_name) /* Name field */               \
                .type = ZBUS_OBSERVER_SUBSCRIBER_TYPE,                        \
                .data = &_CONCAT(_zbus_obs_data_, _name),                     \
                .queue = &_zbus_observer_queue_##_name,                       \
        }
/* clang-format on */

#define ZBUS_SUBSCRIBER_DEFINE(_name, _queue_size)                                                 \
        ZBUS_SUBSCRIBER_DEFINE_WITH_ENABLE(_name, _queue_size, true)

/* clang-format off */

#define ZBUS_LISTENER_DEFINE_WITH_ENABLE(_name, _cb, _enable)                                      \
        static struct zbus_observer_data _CONCAT(_zbus_obs_data_, _name) = {                       \
                .enabled = _enable,                                                                \
                IF_ENABLED(CONFIG_ZBUS_PRIORITY_BOOST, (                                           \
                        .priority = ZBUS_MIN_THREAD_PRIORITY,                                      \
                ))                                                                                 \
        };                                                                                         \
        _ZBUS_CPP_EXTERN const STRUCT_SECTION_ITERABLE(zbus_observer, _name) = {                   \
                ZBUS_OBSERVER_NAME_INIT(_name) /* Name field */                                    \
                .type = ZBUS_OBSERVER_LISTENER_TYPE,                                               \
                .data = &_CONCAT(_zbus_obs_data_, _name),                                          \
                .callback = (_cb)                                                                  \
        }
/* clang-format on */

#define ZBUS_LISTENER_DEFINE(_name, _cb) ZBUS_LISTENER_DEFINE_WITH_ENABLE(_name, _cb, true)

/* clang-format off */

#define ZBUS_MSG_SUBSCRIBER_DEFINE_WITH_ENABLE(_name, _enable)                \
        static K_FIFO_DEFINE(_zbus_observer_fifo_##_name);                    \
        static struct zbus_observer_data _CONCAT(_zbus_obs_data_, _name) = {  \
                .enabled = _enable,                                           \
                IF_ENABLED(CONFIG_ZBUS_PRIORITY_BOOST, (                      \
                        .priority = ZBUS_MIN_THREAD_PRIORITY,                 \
                ))                                                            \
        };                                                                    \
        _ZBUS_CPP_EXTERN const STRUCT_SECTION_ITERABLE(zbus_observer, _name) = {  \
                ZBUS_OBSERVER_NAME_INIT(_name) /* Name field */               \
                .type = ZBUS_OBSERVER_MSG_SUBSCRIBER_TYPE,                    \
                .data = &_CONCAT(_zbus_obs_data_, _name),                     \
                .message_fifo = &_zbus_observer_fifo_##_name,                 \
        }
/* clang-format on */

#define ZBUS_MSG_SUBSCRIBER_DEFINE(_name) ZBUS_MSG_SUBSCRIBER_DEFINE_WITH_ENABLE(_name, true)

#if defined(CONFIG_ZBUS_ASYNC_LISTENER) || defined(__DOXYGEN__)
struct zbus_async_listener_work {
        struct k_work work;
        struct k_fifo *message_fifo;
        struct k_work_q *queue;
        void (*callback)(const struct zbus_channel *chan, const void *msg);
};

void async_listener_work_handler(struct k_work *item);

/* clang-format off */
#define ZBUS_ASYNC_LISTENER_DEFINE_WITH_ENABLE(_name, _cb, _enable)               \
        static K_FIFO_DEFINE(_zbus_observer_work_fifo_##_name);                   \
        static struct zbus_async_listener_work _zbus_observer_work_##_name = {    \
                .work = Z_WORK_INITIALIZER(async_listener_work_handler),          \
                .message_fifo = &_CONCAT(_zbus_observer_work_fifo_, _name),       \
                .queue = &k_sys_work_q,                                           \
                .callback = _cb,                                                  \
        };                                                                        \
        static struct zbus_observer_data _CONCAT(_zbus_obs_data_, _name) = {      \
                .enabled = _enable,                                               \
                IF_ENABLED(CONFIG_ZBUS_PRIORITY_BOOST, (                          \
                        .priority = ZBUS_MIN_THREAD_PRIORITY,                     \
                ))                                                                \
        };                                                                        \
        _ZBUS_CPP_EXTERN const STRUCT_SECTION_ITERABLE(zbus_observer, _name) = {  \
                ZBUS_OBSERVER_NAME_INIT(_name) /* Name field */                   \
                .type = ZBUS_OBSERVER_ASYNC_LISTENER_TYPE,                        \
                .data = &_CONCAT(_zbus_obs_data_, _name),                         \
                .work = &_CONCAT(_zbus_observer_work_, _name).work,               \
        }

#define ZBUS_ASYNC_LISTENER_DEFINE(_name, _cb)                    \
        ZBUS_ASYNC_LISTENER_DEFINE_WITH_ENABLE(_name, _cb, true)
/* clang-format on */

static inline int zbus_async_listener_set_work_queue(const struct zbus_observer *obs,
                                                     struct k_work_q *queue)
{
        CHECKIF(obs == NULL) {
                return -EINVAL;
        }

        CHECKIF(obs->type != ZBUS_OBSERVER_ASYNC_LISTENER_TYPE) {
                return -EINVAL;
        }

        CHECKIF(queue == NULL) {
                return -EINVAL;
        }

        static struct k_spinlock zbus_async_listener_slock;

        K_SPINLOCK(&zbus_async_listener_slock) {
                struct zbus_async_listener_work *async_listener =
                        CONTAINER_OF(obs->work, struct zbus_async_listener_work, work);

                async_listener->queue = queue;
        }
        return 0;
}

#endif /* CONFIG_ZBUS_ASYNC_LISTENER */

int zbus_chan_pub(const struct zbus_channel *chan, const void *msg, k_timeout_t timeout);

int zbus_chan_read(const struct zbus_channel *chan, void *msg, k_timeout_t timeout);

int zbus_chan_claim(const struct zbus_channel *chan, k_timeout_t timeout);

int zbus_chan_finish(const struct zbus_channel *chan);

int zbus_chan_notify(const struct zbus_channel *chan, k_timeout_t timeout);

#if defined(CONFIG_ZBUS_CHANNEL_NAME) || defined(__DOXYGEN__)

static inline const char *zbus_chan_name(const struct zbus_channel *chan)
{
        __ASSERT(chan != NULL, "chan is required");

        return chan->name;
}

#endif

#if defined(CONFIG_ZBUS_CHANNEL_ID) || defined(__DOXYGEN__)

const struct zbus_channel *zbus_chan_from_id(uint32_t channel_id);

#endif

#if defined(CONFIG_ZBUS_CHANNEL_NAME) || defined(__DOXYGEN__)

const struct zbus_channel *zbus_chan_from_name(const char *name);

#endif

#if defined(CONFIG_ZBUS_RUNTIME_CHANNEL_REGISTRATION) || defined(__DOXYGEN__)

static inline void zbus_runtime_channel_init(struct zbus_runtime_channel *chan,
                                             struct zbus_channel_data *data, const char *name,
                                             uint32_t id, zbus_validator validator, void *message,
                                             size_t message_size, void *user_data)
{
        __ASSERT(chan != NULL, "chan is required");
        __ASSERT(data != NULL, "data is required");
        __ASSERT(message != NULL, "message is required");
        __ASSERT(message_size > 0, "message_size must be positive");
#if defined(CONFIG_ZBUS_CHANNEL_NAME)
        __ASSERT(name != NULL, "name is required");
        chan->channel.name = name;
#endif
#if defined(CONFIG_ZBUS_CHANNEL_ID)
        chan->channel.id = id;
#endif
        chan->channel.data = data;
        chan->channel.message = message;
        chan->channel.message_size = message_size;
        chan->channel.validator = validator;
        chan->channel.user_data = user_data;

        memset(data, 0x00, sizeof(*data));
#if defined(CONFIG_ZBUS_PRIORITY_BOOST)
        data->highest_observer_priority = ZBUS_MIN_THREAD_PRIORITY;
#endif
        k_sem_init(&data->sem, 1, 1);
}

int zbus_runtime_channel_register(struct zbus_runtime_channel *chan);

int zbus_runtime_channel_unregister(struct zbus_runtime_channel *chan);

#if defined(CONFIG_ZTEST)

void zbus_runtime_channel_unregister_all(void);

#endif /* CONFIG_ZTEST */

#endif /* CONFIG_ZBUS_RUNTIME_CHANNEL_REGISTRATION */

static inline void *zbus_chan_msg(const struct zbus_channel *chan)
{
        __ASSERT(chan != NULL, "chan is required");

        return chan->message;
}

static inline const void *zbus_chan_const_msg(const struct zbus_channel *chan)
{
        __ASSERT(chan != NULL, "chan is required");

        return chan->message;
}

static inline uint16_t zbus_chan_msg_size(const struct zbus_channel *chan)
{
        __ASSERT(chan != NULL, "chan is required");

        return chan->message_size;
}

static inline void *zbus_chan_user_data(const struct zbus_channel *chan)
{
        __ASSERT(chan != NULL, "chan is required");

        return chan->user_data;
}

#if defined(CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION) || defined(__DOXYGEN__)

static inline void zbus_chan_set_msg_sub_pool(const struct zbus_channel *chan,
                                              struct net_buf_pool *pool)
{
        __ASSERT(chan != NULL, "chan is required");
        __ASSERT(pool != NULL, "pool is required");

        chan->data->msg_subscriber_pool = pool;
}

#endif /* ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION */

#if defined(CONFIG_ZBUS_CHANNEL_PUBLISH_STATS) || defined(__DOXYGEN__)

static inline void zbus_chan_pub_stats_update(const struct zbus_channel *chan)
{
        __ASSERT(chan != NULL, "chan is required");

        chan->data->publish_timestamp = k_uptime_ticks();
        chan->data->publish_count += 1;
}

static inline k_ticks_t zbus_chan_pub_stats_last_time(const struct zbus_channel *chan)
{
        __ASSERT(chan != NULL, "chan is required");

        return chan->data->publish_timestamp;
}

static inline uint32_t zbus_chan_pub_stats_count(const struct zbus_channel *chan)
{
        __ASSERT(chan != NULL, "chan is required");

        return chan->data->publish_count;
}

static inline uint32_t zbus_chan_pub_stats_avg_period(const struct zbus_channel *chan)
{
        __ASSERT(chan != NULL, "chan is required");

        /* Not yet published, period = 0ms */
        if (chan->data->publish_count == 0) {
                return 0;
        }
        /* Average period across application runtime */
        return k_uptime_get() / chan->data->publish_count;
}

static inline uint64_t zbus_chan_pub_stats_msg_age(const struct zbus_channel *chan)
{
        if (zbus_chan_pub_stats_count(chan) == 0) {
                return UINT64_MAX;
        }
        return k_ticks_to_ms_floor64(k_uptime_ticks() - zbus_chan_pub_stats_last_time(chan));
}

#else

static inline void zbus_chan_pub_stats_update(const struct zbus_channel *chan)
{
        (void)chan;
}

#endif /* CONFIG_ZBUS_CHANNEL_PUBLISH_STATS */

#if defined(CONFIG_ZBUS_RUNTIME_OBSERVERS) || defined(__DOXYGEN__)

struct zbus_observer_node {
        sys_snode_t node;
        const struct zbus_observer *obs;
#if defined(CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE)
        const struct zbus_channel *chan;
#endif
};

#if defined(CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE) || defined(__DOXYGEN__)
int zbus_chan_add_obs_with_node(const struct zbus_channel *chan, const struct zbus_observer *obs,
                                struct zbus_observer_node *node, k_timeout_t timeout);
#else
static inline int zbus_chan_add_obs_with_node(const struct zbus_channel *chan,
                                              const struct zbus_observer *obs,
                                              struct zbus_observer_node *node, k_timeout_t timeout)
{
        ARG_UNUSED(chan);
        ARG_UNUSED(obs);
        ARG_UNUSED(node);
        ARG_UNUSED(timeout);

        return -ENOTSUP;
}
#endif /* CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE */

#if !defined(CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE) || defined(__DOXYGEN__)
int zbus_chan_add_obs(const struct zbus_channel *chan, const struct zbus_observer *obs,
                      k_timeout_t timeout);
#else
static inline int zbus_chan_add_obs(const struct zbus_channel *chan,
                                    const struct zbus_observer *obs, k_timeout_t timeout)
{
        ARG_UNUSED(chan);
        ARG_UNUSED(obs);
        ARG_UNUSED(timeout);

        return -ENOTSUP;
}

#endif /* !CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE */
int zbus_chan_rm_obs(const struct zbus_channel *chan, const struct zbus_observer *obs,
                     k_timeout_t timeout);

#endif /* CONFIG_ZBUS_RUNTIME_OBSERVERS */

int zbus_obs_set_enable(const struct zbus_observer *obs, bool enabled);

static inline int zbus_obs_is_enabled(const struct zbus_observer *obs, bool *enable)
{
        _ZBUS_ASSERT(obs != NULL, "obs is required");
        _ZBUS_ASSERT(enable != NULL, "enable is required");

        *enable = obs->data->enabled;

        return 0;
}

int zbus_obs_set_chan_notification_mask(const struct zbus_observer *obs,
                                        const struct zbus_channel *chan, bool masked);

int zbus_obs_is_chan_notification_masked(const struct zbus_observer *obs,
                                         const struct zbus_channel *chan, bool *masked);

#if defined(CONFIG_ZBUS_OBSERVER_NAME) || defined(__DOXYGEN__)

static inline const char *zbus_obs_name(const struct zbus_observer *obs)
{
        __ASSERT(obs != NULL, "obs is required");

        return obs->name;
}

#endif

#if defined(CONFIG_ZBUS_PRIORITY_BOOST) || defined(__DOXYGEN__)

int zbus_obs_attach_to_thread(const struct zbus_observer *obs);

int zbus_obs_detach_from_thread(const struct zbus_observer *obs);

#endif /* CONFIG_ZBUS_PRIORITY_BOOST */

int zbus_sub_wait(const struct zbus_observer *sub, const struct zbus_channel **chan,
                  k_timeout_t timeout);

#if defined(CONFIG_ZBUS_MSG_SUBSCRIBER) || defined(__DOXYGEN__)

int zbus_sub_wait_msg(const struct zbus_observer *sub, const struct zbus_channel **chan, void *msg,
                      k_timeout_t timeout);

#endif /* CONFIG_ZBUS_MSG_SUBSCRIBER */

bool zbus_iterate_over_channels(bool (*iterator_func)(const struct zbus_channel *chan));
bool zbus_iterate_over_channels_with_user_data(
        bool (*iterator_func)(const struct zbus_channel *chan, void *user_data), void *user_data);

bool zbus_iterate_over_observers(bool (*iterator_func)(const struct zbus_observer *obs));
bool zbus_iterate_over_observers_with_user_data(
        bool (*iterator_func)(const struct zbus_observer *obs, void *user_data), void *user_data);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_ZBUS_ZBUS_H_ */
```

## 212.2\_可见自然语言注释

| 原注释 | 中文说明 |
| --- | --- |
| `No runtime observers` | 没有运行时观察者 |
| `are there zero non-empty arguments ?` | 非空参数的数量是否为零？ |
| `if so, expand to nothing` | 如果是，则展开为空 |
| `otherwise, expand to:` | 否则展开为后面的内容 |
| `plus a final terminator` | 再加上末尾终止符 |
| `Maybe removed` | 可能被移除；这里对应可由配置省去的名称初始化字段 |
| `Extern declaration of observers` | 观察者的外部声明 |
| `Create all channel observations from observers list` | 根据观察者列表创建全部通道观察关系 |
| `Name field` | 名称字段 |
| `Not yet published, period = 0ms` | 尚未发布，周期为0毫秒 |
| `Average period across application runtime` | 按应用运行时间计算平均周期 |
| `clang-format off``clang-format on` | 关闭／恢复 clang-format 源码格式化处理 |

其他注释中的`CONFIG_`名称及末尾头文件保护宏（Header Guard）是对应条件分支的结束标记。`__cplusplus`用于 C++ 的 C 语言链接约定，`__DOXYGEN__`用于文档生成。

## 212.3\_断言文本与可见条件分支

断言（Assertion）中的`chan is required``data is required``message is required``name is required``pool is required``obs is required``enable is required`分别表示必须提供对应的通道、数据、消息、名称、缓冲池、观察者或启用状态输出指针，不能为`NULL`。`message_size must be positive`表示消息大小必须为正数。`ZBUS ASSERT:`是 zbus 断言信息前缀。

`CONFIG_ZBUS_ASSERT_MOCK`分支在检查失败时输出信息并返回`-EFAULT`，其他分支调用`__ASSERT`。`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE`决定使用调用者提供的节点还是由接口分配节点；不支持的接口分支返回`-ENOTSUP`。

发布统计（Publish Statistics）启用时会保存内核时钟节拍（Kernel Tick）时间戳和发布计数；关闭时仍保留一个无操作的`zbus_chan_pub_stats_update`内联函数。平均周期计算使用`k_uptime_get() / publish_count`，消息年龄换算为毫秒；尚未发布时消息年龄返回`UINT64_MAX`。

`CONFIG_ZBUS_RUNTIME_CHANNEL_REGISTRATION`控制运行时通道注册接口；其内的`CONFIG_ZTEST`分支额外声明`zbus_runtime_channel_unregister_all`。异步监听器由`CONFIG_ZBUS_ASYNC_LISTENER`控制，初始使用`k_sys_work_q`系统工作队列。

## 212.4\_保留原文与实现差异

可见源码中，异步监听器设置工作队列时的三个错误检查均返回`-EINVAL`，而 API 文档对两个空指针条件分别写成`-ENOENT`和`-EBADF`。`zbus_obs_is_enabled`正常返回0，并通过输出指针写出启用状态。

观察者说明中的通道“索引”、消息订阅者宏的类型名称、附加线程的成功描述，以及消息初始化宏示例的名称，也与对应声明存在差异。详细译注集中在[zbus观察者结构](P208_zbus观察者结构.md)和[zbus核心接口](P213_zbus核心接口.md)，原始代码未因这些差异而修改。

---

[上一章：zbus核心头文件参考](P211_zbus核心头文件参考.md) · [下一章：zbus核心接口](P213_zbus核心接口.md) · [返回大纲](大纲.md)
