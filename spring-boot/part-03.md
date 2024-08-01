# Create and setup spring boot

- [spring initializer](https://start.spring.io/)
- Project = Maven
- Spring boot - 3.3.2
- Project Meta data
  - packaging
    - jar
  - java
    - 22
- Dependencies
  - Spring Web : RestFull app using MVC, Embedded apache Tomcat server
  - Spring Data JPA : Java Persistence API, uses Hibernate.
  - MySQL Driver : driver to connect to MySQL database.
  - Lombok : don't have to write much code.

## other notes

### Gradle vs Maven

- Gradle and Maven are both Java development tools that can handle dynamic and transitive dependencies and support parallel execution of multi-module builds. However, they differ in their approach to builds and have other differences:
- Performance: Gradle is generally faster than Maven, especially when building incremental changes or when task outputs can be resolved using Gradle's build cache. Gradle's incrementality feature avoids work by tracking input and output of tasks and only running what is necessary.
- Plugins and integrations: Maven has more plugins available than Gradle.
- Flexibility: Gradle is more flexible and based on a script, while Maven is structured and can be less flexible in certain scenarios.
- Ease of use: Maven is user-friendly due to its conventions

### why to use com.example

Companies use their reversed Internet domain name to begin their package names—for example, com. example. mypackage for a package named mypackage created by a programmer at example.com
