import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProductList = () => {
    const [products, setProducts] = useState([]);
    const [searchQuery, setSearchQuery] = useState('');
    const [categoryFilter, setCategoryFilter] = useState('');
    const [tagFilters, setTagFilters] = useState([]);
    const [categories, setCategories] = useState([]);
    const [tags, setTags] = useState([]);

    useEffect(() => {
        const addQuery = (query) => {
            if (query) {
                query += '&'
            } else {
                query += '?'
            }
            return query
        }

        const fetchData = async () => {
            let url = 'http://localhost:8000/api/products/';
            let query = ''
            if (searchQuery) {
                query += `?search=${searchQuery}`;
            }
            if (categoryFilter) {
                query = addQuery(query)
                query += `category=${categoryFilter}`;
            }

            if (tagFilters.length) {
                tagFilters.forEach(tag => {
                    query = addQuery(query)
                    query += `tag=${tag.id}`
                })
            }
            const result = await axios.get(url + query);
            setProducts(result.data);
        };
        fetchData();
    }, [searchQuery, categoryFilter, tagFilters]);

    useEffect(() => {
        const fetchCategories = async () => {
            const result = await axios.get('http://localhost:8000/api/categories/');
            setCategories(result.data);
        };
        fetchCategories();
    }, []);

    useEffect(() => {
        const fetchTags = async () => {
            const result = await axios.get('http://localhost:8000/api/tags/');
            setTags(result.data);
        };
        fetchTags();
    }, []);

    return (
        <div>
            <h2>Product List</h2>
            <ul>
                <p>Selected tags(click to delete tag):</p>
                {tagFilters.map((tag, index) =>
                    <li key={tag.id} onClick={() => {
                        tagFilters.splice(index, 1)
                        setTagFilters([...tagFilters])
                    }}>
                        {tag.name}
                    </li>
                )}
            </ul>
            <input
                type="text"
                value={searchQuery}
                onChange={e => setSearchQuery(e.target.value)}
                placeholder="Search by name"
            />
            <select
                value={categoryFilter}
                onChange={e => setCategoryFilter(e.target.value)}
            >
                <option value="">Select category</option>
                {categories.map(category => (
                    <option key={category.id} value={category.id}>{category.name}</option>
                ))}
            </select>
            <select
                value={tagFilters}
                onChange={e => {
                    const id = e.target.value.split('/')[0]
                    const name = e.target.value.split('/')[1]
                    tagFilters.push({id, name})
                    return setTagFilters([...tagFilters])
                }}
            >
                <option value="">Add tag</option>
                {tags.map(tag => (
                    <option key={tag.id} value={tag.id + '/' + tag.name}>{tag.name}</option>
                ))}
            </select>
            <ul style={{marginBottom: '10px'}}>
                {products.map(product => (
                    <>
                        <li key={product.id}>Product: <span style={{fontWeight: '600'}}>{product.name}</span></li>
                        <p>Category: <span style={{fontWeight: '600'}}>{product.category.name}</span></p>
                        <p>Tags: </p>
                        <ul>
                            {product.tags.map(tag => (
                                <li key={tag.id}>{tag.name}</li>
                            ))}
                        </ul>
                    </>
                ))}
            </ul>
        </div>
    );
};

export default ProductList;
