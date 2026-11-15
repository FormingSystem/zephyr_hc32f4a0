/*
 * SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
 * SPDX-License-Identifier: Apache-2.0
 */

#include <errno.h>
#include <stddef.h>
#include <stdint.h>
#include <zephyr/ztest.h>

#define RECORD_CAPACITY 3U

/** @brief 拥有三个采样值存储空间的记录，count 表示已初始化的有效元素数。 */
struct sample_record {
	uint16_t values[RECORD_CAPACITY];
	size_t count;
};

/** @brief 只借用其他对象的元素，不拥有、也不延长其存储期。 */
struct sample_view {
	const uint16_t *values;
	size_t count;
};

/** @brief 同步处理函数类型：仅在调用期间借用记录和调用方提供的状态。 */
typedef int (*record_consumer_t)(const struct sample_record *record, void *context);

/** @brief 接收方拥有独立记录，calls 记录当前测试内的同步调用次数。 */
struct collector {
	struct sample_record saved;
	unsigned int calls;
};

/**
 * @brief 将有效输入复制到目标记录；失败时不改写目标。
 * @param destination 调用期间有效且可写的目标记录。
 * @param values 指向至少 count 个有效元素；本教学接口不接受空指针。
 * @param count 要复制的元素数，不能大于记录容量。
 * @return 成功为 0，空指针为 -EINVAL，容量不足为 -ENOSPC。
 */
static int record_load(struct sample_record *destination, const uint16_t *values,
		       size_t count)
{
	struct sample_record candidate = {0};

	if (destination == NULL || values == NULL) {
		return -EINVAL;
	}
	if (count > RECORD_CAPACITY) {
		return -ENOSPC;
	}

	for (size_t i = 0; i < count; ++i) {
		candidate.values[i] = values[i];
	}
	candidate.count = count;
	/* 先准备完整新值，再一次赋给目标，失败分支不会留下半条记录。 */
	*destination = candidate;
	return 0;
}

/** @brief 检查描述符和下标后才读取；调用者仍须保证借用对象在整个调用中存活。 */
static int view_read(const struct sample_view *view, size_t index, uint16_t *output)
{
	if (view == NULL || view->values == NULL || output == NULL) {
		return -EINVAL;
	}
	if (index >= view->count) {
		return -ERANGE;
	}

	*output = view->values[index];
	return 0;
}

/** @brief 局部记录按值返回，返回的是值而不是局部对象的地址。 */
static struct sample_record make_record(void)
{
	struct sample_record local = {
		.values = {10, 20, 30},
		.count = RECORD_CAPACITY,
	};

	return local;
}

/** @brief 名字只在此函数块中可见，对象的静态存储期却覆盖整个程序运行。 */
static uint16_t *persistent_cell(void)
{
	static uint16_t cell;

	return &cell;
}

/** @brief 在返回前完成一次回调，不保存 record、consumer 或 context。 */
static int deliver_now(const struct sample_record *record, record_consumer_t consumer,
		       void *context)
{
	if (record == NULL || consumer == NULL || context == NULL) {
		return -EINVAL;
	}
	if (record->count > RECORD_CAPACITY) {
		return -EINVAL;
	}

	return consumer(record, context);
}

/** @brief 在借用结束前复制有效记录，后续读取 saved 不再依赖原记录。 */
static int collect_record(const struct sample_record *record, void *context)
{
	struct collector *collector = context;

	collector->saved = *record;
	++collector->calls;
	return 0;
}

/** @brief 用定义良好的错误返回模拟接收方拒绝，不执行非法内存访问。 */
static int reject_record(const struct sample_record *record, void *context)
{
	unsigned int *calls = context;

	(void)record;
	++*calls;
	return -EIO;
}

ZTEST(c_lifetime, test_return_value_survives_local_object)
{
	struct sample_record received = make_record();

	zassert_equal(received.count, 3U);
	zassert_equal(received.values[0], 10U);
	zassert_equal(received.values[1], 20U);
	zassert_equal(received.values[2], 30U);
}

ZTEST(c_lifetime, test_structure_copy_owns_embedded_array)
{
	struct sample_record original = make_record();
	struct sample_record snapshot = original;

	original.values[0] = 99;
	original.count = 1;
	zassert_equal(snapshot.values[0], 10U);
	zassert_equal(snapshot.count, 3U);
	zassert_equal(original.values[0], 99U);
	zassert_equal(original.count, 1U);
}

ZTEST(c_lifetime, test_pointer_copy_still_borrows_original)
{
	struct sample_record original = make_record();
	struct sample_view view = {original.values, original.count};
	struct sample_view second = view;
	uint16_t observed = 0;

	zassert_equal_ptr(view.values, second.values);
	original.values[1] = 77;
	zassert_ok(view_read(&second, 1, &observed));
	zassert_equal(observed, 77U);
	/* 借用的退出动作在原对象仍存活时执行，不能在失效后比较旧指针。 */
	view.values = NULL;
	view.count = 0;
	second.values = NULL;
	second.count = 0;
	zassert_equal(view_read(&second, 0, &observed), -EINVAL);
	zassert_equal(observed, 77U);
}

ZTEST(c_lifetime, test_block_scope_static_object_persists)
{
	uint16_t *first = persistent_cell();

	*first = 41;
	uint16_t *second = persistent_cell();

	zassert_equal_ptr(first, second);
	++*second;
	zassert_equal(*first, 42U);
}

ZTEST(c_lifetime, test_bounds_and_null_fail_before_access)
{
	struct sample_record original = make_record();
	struct sample_view view = {original.values, original.count};
	uint16_t observed = 500;

	zassert_equal(view_read(&view, 3, &observed), -ERANGE);
	zassert_equal(observed, 500U);
	zassert_equal(view_read(NULL, 0, &observed), -EINVAL);
	zassert_equal(view_read(&view, 0, NULL), -EINVAL);
	zassert_equal(observed, 500U);
	zassert_ok(view_read(&view, 2, &observed));
	zassert_equal(observed, 30U);
}

ZTEST(c_lifetime, test_capacity_failure_preserves_destination)
{
	const uint16_t input[] = {4, 5, 6, 7};
	struct sample_record destination = make_record();

	zassert_equal(record_load(&destination, input, 4), -ENOSPC);
	zassert_equal(destination.count, 3U);
	zassert_equal(destination.values[0], 10U);
	zassert_equal(destination.values[1], 20U);
	zassert_equal(destination.values[2], 30U);
	zassert_equal(record_load(&destination, NULL, 0), -EINVAL);
	zassert_equal(destination.values[0], 10U);
	zassert_ok(record_load(&destination, input, 3));
	zassert_equal(destination.count, 3U);
	zassert_equal(destination.values[0], 4U);
	zassert_equal(destination.values[2], 6U);
}

ZTEST(c_lifetime, test_synchronous_callback_copies_before_return)
{
	struct collector receiver = {0};

	{
		struct sample_record temporary = make_record();

		zassert_ok(deliver_now(&temporary, collect_record, &receiver));
		zassert_equal(receiver.calls, 1U);
		temporary.values[0] = 88;
		zassert_equal(receiver.saved.values[0], 10U);
	}
	/* temporary 已结束生命期，此处只访问 receiver 自己拥有的数组。 */
	zassert_equal(receiver.saved.values[0], 10U);
	zassert_equal(receiver.saved.values[2], 30U);
}

ZTEST(c_lifetime, test_callback_error_propagates_without_retry)
{
	struct sample_record original = make_record();
	unsigned int calls = 0;

	zassert_equal(deliver_now(&original, reject_record, &calls), -EIO);
	zassert_equal(calls, 1U);
	zassert_equal(deliver_now(&original, NULL, &calls), -EINVAL);
	zassert_equal(deliver_now(NULL, reject_record, &calls), -EINVAL);
	zassert_equal(deliver_now(&original, reject_record, NULL), -EINVAL);
	zassert_equal(calls, 1U);
	zassert_equal(original.values[0], 10U);
}

ZTEST_SUITE(c_lifetime, NULL, NULL, NULL, NULL, NULL);
