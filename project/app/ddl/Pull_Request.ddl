CREATE TABLE IF NOT EXISTS PullRequest (
    repository VARCHAR(255),
    title VARCHAR(255),
    st_pull_request_url VARCHAR(1000),
    e2e_pull_request_url VARCHAR(1000),
    main_pull_request_url VARCHAR(1000),

    source_branch VARCHAR(512),
    target_branch VARCHAR(255),

    pull_request_id INT PRIMARY KEY

);
