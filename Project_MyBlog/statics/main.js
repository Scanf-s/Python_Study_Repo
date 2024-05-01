function fetchPosts() {
        axios.get('/posts/')
            .then(function (response) {
                const posts = response.data;
                let postsHtml = posts.map(post => `
                    <div class="card mt-3">
                        <div class="card-body">
                            <h5 class="card-title">${post.title}</h5>
                            <p class="card-text">${post.content}</p>
                            <p class="text-muted">Posted on ${new Date(post.created_at).toLocaleDateString()}</p>
                            <button class="btn btn-warning" onclick="editPost(${post.id})">Edit</button>
                            <button class="btn btn-danger" onclick="deletePost(${post.id})">Delete</button>
                        </div>
                    </div>
                `).join('');
                document.getElementById('postsContainer').innerHTML = postsHtml;
            })
            .catch(function (error) {
                console.log(error);
            });
}

document.getElementById('addPostForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;
    axios.post('/posts/', { title: title, content: content })
        .then(function (response) {
            console.log(response);
            fetchPosts();  // Refresh posts list
        })
        .catch(function (error) {
            console.log(error);
        });
});

function editPost(postId) {
    const title = prompt("Enter new title:");
    const content = prompt("Enter new content:");
    if (title && content) {
        axios.put(`/posts/${postId}`, { title: title, content: content })
            .then(function (response) {
                console.log(response);
                fetchPosts();
            })
            .catch(function (error) {
                console.log(error);
            });
    }
}

function deletePost(postId) {
    if (confirm("Are you sure you want to delete this post?")) {
        axios.delete(`/posts/${postId}`)
            .then(function (response) {
                console.log(response);
                fetchPosts();
            })
            .catch(function (error) {
                console.log(error);
            });
    }
}