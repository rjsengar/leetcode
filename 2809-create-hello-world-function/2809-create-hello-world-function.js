/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        n="Hello World";
        return n
        
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */