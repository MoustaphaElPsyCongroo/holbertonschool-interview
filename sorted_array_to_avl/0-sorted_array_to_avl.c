#include "binary_trees.h"

/**
 * create - Creates a binary tree
 * @parent: Pointer to the parent node
 * @value: Integer stored
 * Return: Pointer to the new node
 */

binary_tree_t *create(binary_tree_t *parent, int value)
{
	binary_tree_t *new;

	new = malloc(sizeof(binary_tree_t));
	if (new == NULL)
		return (NULL);
	new->parent = parent;
	new->left = NULL;
	new->right = NULL;
	new->n = value;
	return (new);
}
/**
 * create_avl - AVL tree node
 * @array: first element of the array
 * @start: Index of the first element
 * @end: Index of the last element
 * @parent: Pointer to the parent node
 * Return: Pointer to the root node
 */
avl_t *create_avl(int *array, int start, int end, avl_t *parent)
{
	avl_t *new_node = NULL;
	int mid = 0;

	if (start > end)
		return (NULL);

	mid = (start + end) / 2;
	new_node = create(parent, array[mid]);
	if (new_node == NULL)
		return (NULL);

	new_node->parent = parent;
	new_node->left = create_avl(array, start, mid - 1, new_node);
	new_node->right = create_avl(array, mid + 1, end, new_node);

	return (new_node);
}

/**
 * sorted_array_to_avl - Builds an AVL tree from a sorted array
 * @array: Pointer to the first element of the array to be converted
 * @size: Number of elements in the array
 * Return: Pointer to the root node or NULL on failure
 */
avl_t *sorted_array_to_avl(int *array, size_t size)
{
	avl_t *root = NULL;

	if (array == NULL || size == 0)
		return (NULL);

	root = create_avl(array, 0, size - 1, NULL);
	return (root);
}
