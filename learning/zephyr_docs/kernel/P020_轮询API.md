---
id: learning.zephyr-docs.kernel.polling
title: 轮询API
kind: reference
status: maintained
domains: [zephyr, kernel, polling]
source_url: https://docs.zephyrproject.org/latest/kernel/services/polling.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第20章\_轮询API

原文：[Polling API](https://docs.zephyrproject.org/latest/kernel/services/polling.html)。读取日期：2026-10-12，`latest`。

**轮询接口（Polling API）**用于同时等待多个条件中的任意一个满足。主要函数 `k_poll()` 的概念与 POSIX 的 `poll()` 相似，但它操作内核对象，而不是文件描述符。单个线程即可等待多个条件，无须主动逐个反复检查。

## 20.1\_支持的条件与事件数组

原文当前支持以下条件：信号量可用，内核 **先进先出（First In, First Out，FIFO）**、**后进先出（Last In, First Out，LIFO）**、消息队列或管道中已有可取数据，以及 poll signal 被触发。

线程要同时等待多个条件，需定义一个轮询事件数组，每个条件对应一个事件。轮询前必须初始化全部条目，指定：应满足的条件类型、对应的内核对象、条件满足后的操作模式。还可自定义 tag，把相关事件分组。除真实内核对象外，还有能直接触发的轮询信号伪对象。

任一条件满足，`k_poll()` 就返回。返回时可能有多个条件满足，例如调用前已经就绪，或抢占式调度使其他条件在返回前也满足。调用者应检查数组中所有事件的 `state`，再决定处理动作。

当前唯一模式是**只通知、不取得对象**。例如事件显示信号量可用后，仍须调用 `k_sem_take()` 真正获取。若有竞争，实际 take 时不保证仍可用。

## 20.2\_初始化轮询事件

事件类型为 `struct k_poll_event`，数组每项表示一个条件。可用运行时初始化器 `K_POLL_EVENT_INITIALIZER()`、函数 `k_poll_event_init()`，或静态初始化器 `K_POLL_EVENT_STATIC_INITIALIZER()`。

传入对象必须匹配事件类型，模式设为 `K_POLL_MODE_NOTIFY_ONLY`，初始状态为 `K_POLL_STATE_NOT_READY`（初始化器会设置）。tag 完全由应用解释，接口不理解其含义。静态初始化器接受 tag；运行时初始化器为了避免额外开销不传 tag，需要时应用自行设置。若暂时忽略某项，可把其类型设为 `K_POLL_TYPE_IGNORE`。

下面静态初始化四个事件，分别等待信号量、FIFO、消息队列和管道：

```c
struct k_poll_event events[4] = {
    K_POLL_EVENT_STATIC_INITIALIZER(K_POLL_TYPE_SEM_AVAILABLE,
                                    K_POLL_MODE_NOTIFY_ONLY,
                                    &my_sem, 0),
    K_POLL_EVENT_STATIC_INITIALIZER(K_POLL_TYPE_FIFO_DATA_AVAILABLE,
                                    K_POLL_MODE_NOTIFY_ONLY,
                                    &my_fifo, 0),
    K_POLL_EVENT_STATIC_INITIALIZER(K_POLL_TYPE_MSGQ_DATA_AVAILABLE,
                                    K_POLL_MODE_NOTIFY_ONLY,
                                    &my_msgq, 0),
    K_POLL_EVENT_STATIC_INITIALIZER(K_POLL_TYPE_PIPE_DATA_AVAILABLE,
                                    K_POLL_MODE_NOTIFY_ONLY,
                                    &my_pipe, 0),
};
```

也可在运行时完成同样配置：

```c
struct k_poll_event events[4];
void some_init(void)
{
    k_poll_event_init(&events[0],
                      K_POLL_TYPE_SEM_AVAILABLE,
                      K_POLL_MODE_NOTIFY_ONLY,
                      &my_sem);

    k_poll_event_init(&events[1],
                      K_POLL_TYPE_FIFO_DATA_AVAILABLE,
                      K_POLL_MODE_NOTIFY_ONLY,
                      &my_fifo);

    k_poll_event_init(&events[2],
                      K_POLL_TYPE_MSGQ_DATA_AVAILABLE,
                      K_POLL_MODE_NOTIFY_ONLY,
                      &my_msgq);

    k_poll_event_init(&events[3],
                      K_POLL_TYPE_PIPE_DATA_AVAILABLE,
                      K_POLL_MODE_NOTIFY_ONLY,
                      &my_pipe);

    // tags are left uninitialized if unused
}
```

## 20.3\_调用k_poll

初始化后，将数组传给 `k_poll()`。可指定等待时限，`K_NO_WAIT` 表示不等待，`K_FOREVER` 表示持续等待条件满足。

原文说明每个信号量或 FIFO 提供 poller 列表，可容纳应用所需的多个轮询事件；轮询等待者按先到先服务处理，而不是按线程优先级。成功返回 0，超时返回 `-EAGAIN`。

下面例子等待最多 1000 毫秒，再尝试取得就绪对象：

```c
// assume there is no contention on this semaphore and FIFO
// -EADDRINUSE will not occur; the semaphore and/or data will be available

void do_stuff(void)
{
    rc = k_poll(events, ARRAY_SIZE(events), K_MSEC(1000));
    if (rc == 0) {
        if (events[0].state == K_POLL_STATE_SEM_AVAILABLE) {
            k_sem_take(events[0].sem, 0);
        } else if (events[1].state == K_POLL_STATE_FIFO_DATA_AVAILABLE) {
            data = k_fifo_get(events[1].fifo, 0);
            // handle data
        } else if (events[2].state == K_POLL_STATE_MSGQ_DATA_AVAILABLE) {
            ret = k_msgq_get(events[2].msgq, buf, K_NO_WAIT);
            // handle data
        } else if (events[3].state == K_POLL_STATE_PIPE_DATA_AVAILABLE) {
            bytes_read = k_pipe_read(events[3].pipe, buf, bytes_to_read, K_NO_WAIT);
            // handle data
        }
    } else {
        // handle timeout
    }
}
```

> 译注：原例注释残留 `-EADDRINUSE` 及单等待者时代的描述，不能据此否定前文明确写出的 poller 列表行为。原例传给 `k_sem_take()`、`k_fifo_get()` 的整数 `0` 是旧写法，当前超时类型应使用 `K_NO_WAIT`。它还使用 `else if`，一次只处理首个匹配项；需要处理所有就绪条件时应逐项独立检查，并核对实际 take/get/read 的返回值。示例中的变量与缓冲区由应用补充。

## 20.4\_循环轮询

在循环中重复调用时，应用必须把事件状态恢复为 `K_POLL_STATE_NOT_READY`。下例分别检查各项，然后重置状态：

```c
void do_stuff(void)
{
    for(;;) {
        rc = k_poll(events, ARRAY_SIZE(events), K_FOREVER);
        if (events[0].state == K_POLL_STATE_SEM_AVAILABLE) {
            k_sem_take(events[0].sem, 0);
        }
        if (events[1].state == K_POLL_STATE_FIFO_DATA_AVAILABLE) {
            data = k_fifo_get(events[1].fifo, 0);
            // handle data
        }
        if (events[2].state == K_POLL_STATE_MSGQ_DATA_AVAILABLE) {
            ret = k_msgq_get(events[2].msgq, buf, K_NO_WAIT);
            // handle data
        }
        if (events[3].state == K_POLL_STATE_PIPE_DATA_AVAILABLE) {
            bytes_read = k_pipe_read(events[3].pipe, buf, bytes_to_read, K_NO_WAIT);
            // handle data
        }
        events[0].state = K_POLL_STATE_NOT_READY;
        events[1].state = K_POLL_STATE_NOT_READY;
        events[2].state = K_POLL_STATE_NOT_READY;
        events[3].state = K_POLL_STATE_NOT_READY;
    }
}
```

> 译注：本例展示状态重置，仍省略部分错误检查，且包含前述整数超时旧写法。就绪通知不是对象所有权，不能在竞争场景下假定后续读取一定成功。

## 20.5\_轮询信号

`K_POLL_TYPE_SIGNAL` 表示可以直接触发的轮询事件，可把它理解为仅供一个线程等待的轻量二值信号。

信号本身是独立的 `struct k_poll_signal` 对象，像信号量或 FIFO 一样关联到轮询事件。使用前通过 `K_POLL_SIGNAL_INITIALIZER()` 或 `k_poll_signal_init()` 初始化：

```c
struct k_poll_signal signal;
void do_stuff(void)
{
    k_poll_signal_init(&signal);
}
```

`k_poll_signal_raise()` 触发信号，还携带由应用解释的 `result` 值，向等待线程传递附加信息。下面线程 A 等待，线程 B 发送 `0x1337`，线程 A 用 `k_poll_signal_check()` 读取触发状态和结果：

```c
struct k_poll_signal signal;

// thread A
void do_stuff(void)
{
    k_poll_signal_init(&signal);

    struct k_poll_event events[1] = {
        K_POLL_EVENT_INITIALIZER(K_POLL_TYPE_SIGNAL,
                                 K_POLL_MODE_NOTIFY_ONLY,
                                 &signal),
    };

    k_poll(events, 1, K_FOREVER);

    int signaled, result;

    k_poll_signal_check(&signal, &signaled, &result);

    if (signaled && (result == 0x1337)) {
        // A-OK!
    } else {
        // weird error
    }
}

// thread B
void signal_do_stuff(void)
{
    k_poll_signal_raise(&signal, 0x1337);
}
```

## 20.6\_循环使用信号与丢失通知

循环轮询时，若信号已触发，每轮都要调用 `k_poll_signal_reset()` 复位信号，并把对应事件的 `state` 设回 `K_POLL_STATE_NOT_READY`：

```c
struct k_poll_signal signal;
void do_stuff(void)
{
    k_poll_signal_init(&signal);

    struct k_poll_event events[1] = {
        K_POLL_EVENT_INITIALIZER(K_POLL_TYPE_SIGNAL,
                                 K_POLL_MODE_NOTIFY_ONLY,
                                 &signal),
    };

    for (;;) {
        k_poll(events, 1, K_FOREVER);

        int signaled, result;

        k_poll_signal_check(&signal, &signaled, &result);

        if (signaled && (result == 0x1337)) {
            // A-OK!
        } else {
            // weird error
        }

        k_poll_signal_reset(&signal);
        events[0].state = K_POLL_STATE_NOT_READY;
    }
}
```

原文提醒轮询信号没有替应用提供完整的内部同步协议。系统某处调用 raise 后，等待该信号的 `k_poll()` 会返回；但若信号又被其他代码初始化或重置，等应用检查时触发状态可能已经消失，简单实现就会漏事件。

最佳做法是只在执行 `k_poll()` 循环的线程内重置信号，或改用可保留事件数量的数据类型，例如信号量、FIFO。相较仅有一个触发标志的信号，它们更容易避免覆盖通知。

> 译注：`k_poll_signal_reset()` 复位的是触发标志，不应依赖它把 `result` 清零；只有检查到有效触发后才解释结果。信号量仍受计数上限限制，FIFO 仍须保证内存与入队成功，原文所称“不漏事件”不能理解为不受资源约束的无限保存保证。

## 20.7\_用途、限制与配置

用一个 `k_poll()` 线程替代多个“各等一个对象”的线程，可节省大量线程栈空间。只有一个等待者时，轮询信号也可作为轻量二值通知。

原文末尾建议把轮询用于低竞争对象：一个线程充当多个对象的主服务者或分发者，并由它独自获取这些对象。直接等待对象的线程通常先于轮询通知获得资源，因此轮询不能取代获取时的竞争处理。

> 译注：该末尾注意事项还写“同一对象只能有一个线程轮询”，与前文多 poller 列表相矛盾，属于页面内部不一致。这里保留其低竞争使用建议，但不将旧的单 poller 限制作为当前通用结论。请以目标版本的接口与实现为准。

相关 Kconfig 选项为 `CONFIG_POLL`，完整参考见[异步轮询 API](../eventpoll_reference/P003_轮询公共接口.md)。

> 译注——当前接口与初始化：poll.c按单一类型值分派，不支持任意组合不同类型位；FIFO／LIFO／QUEUE的数据可用类型是相同值的别名。动态信号初始化不设置result，信号reset也不清除事件数组的state。上面的原始示例把signaled声明为int，而当前check接口要求unsigned int指针；实际程序应分别声明unsigned int signaled和int result。完整声明见[轮询公共接口](../eventpoll_reference/P003_轮询公共接口.md)。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：环形缓冲区](P019_环形缓冲区.md) · [本模块主线目录](../reading/kernel.md) · [全部主线](../reading/README.md) · [下一篇：内存管理入口](P021_内存管理入口.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：环形缓冲区](P019_环形缓冲区.md) · [下一章：内存管理入口](P021_内存管理入口.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
